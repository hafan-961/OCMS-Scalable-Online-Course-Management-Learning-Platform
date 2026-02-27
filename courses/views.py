from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404
from .models import Category, Course, Module, Lecture
from .serializers import CategorySerializer, CourseSerializer, ModuleSerializer, LectureSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) 
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@cache_page(900) 
@api_view(['GET'])
@permission_classes([AllowAny]) 
def course_list_public(request):
    courses = Course.objects.filter(is_published=True)
    
    #filtering logic
    level = request.query_params.get('level')
    category = request.query_params.get('category_id')
    if level:
        courses = courses.filter(level=level)
    if category:
        courses = courses.filter(category_id=category)

    #ordering logic
    ordering = request.query_params.get('ordering')
    if ordering:
        courses = courses.order_by(ordering)

    #pagination logic 
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(courses, request)
    serializer = CourseSerializer(result_page, many=True)
    
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def course_create(request):
    #only instructors should create courses (logic check)
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    # protected methods
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Instructor Dashboard
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def instructor_courses(request):

    courses = Course.objects.filter(instructor_id=request.user.id)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def module_list_create(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'GET':
        modules = Module.objects.filter(course_id=course_id).order_by('order')
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated or request.user.id != course.instructor_id.id:
            return Response({"detail": "Only the instructor of this course can add modules."}, status=403)
        
        data = request.data.copy()
        data['course_id'] = course_id
        serializer = ModuleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def lecture_list_create(request, module_id):
    module = get_object_or_404(Module, pk=module_id)

    if request.method == 'GET':
        lectures = Lecture.objects.filter(module_id=module_id).order_by('order')
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated or request.user.id != module.course_id.instructor_id.id:
            return Response({"detail": "Only the instructor can add lectures."}, status=403)

        data = request.data.copy()
        data['module_id'] = module_id
        serializer = LectureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def lecture_detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)

    if request.method == 'GET':
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)

    if not request.user.is_authenticated or request.user.id != lecture.module_id.course_id.instructor_id.id:
        return Response({"detail": "Unauthorized"}, status=403)

    if request.method == 'PUT':
        serializer = LectureSerializer(lecture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lecture.delete()
        return Response(status=204)