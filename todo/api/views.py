from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Task
from api.serializers import TaskSerializer
from rest_framework import status
from logging import getLogger


logger = getLogger('django')


class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer

    def list(self, request):
        """ List all tasks """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        logger.info(f"Tasks: {serializer.data}")
        return Response(serializer.data)

    def create(self, request, ):
        """ Create a new task """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Task created: {serializer.data}")
            return Response({'message': 'Task created successfully!'}, status=status.HTTP_201_CREATED)
        logger.info(f"Task creation failed: {serializer.errors}")
        return Response(serializer.errors)

    def patch(self, request, pk):
        """ Update complete status of a task"""
        try:
            task = Task.objects.get(id=pk)
            if task.complete:
                task.complete = False
            else:
                task.completed = True
            task.save()
            logger.info(f"Task completed successfully!: {task.completed}")
            return Response({'message': 'Task completed successfully!'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            logger.info(f"Task completion failed!: id {pk}")
            return Response({'message': 'Task completion failed!'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """ Delete a task """
        try:
            task = Task.objects.get(id=pk)
            logger.info(f"Task deleted successfully!: id {task.id}")
            task.delete()
            return Response({'message': 'Task deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            logger.info(f"Task deletion failed! id {pk}")
            return Response({'message': 'Task deletion failed!'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def filter(self, request):
        """ Filter tasks by date and contanin or only date or contain"""
        date = request.query_params.get('fecha')
        content = request.query_params.get('content')
        if not (date or content):
            logger.info(f"Filter tasks failed: {date} or {content}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if date and content:
            tasks = Task.objects.filter(
                fecha__contains=date, content__contains=content)
        elif date:
            tasks = Task.objects.filter(fecha__contains=date)
        else:
            tasks = Task.objects.filter(content__contains=content)
        serializer = TaskSerializer(tasks, many=True)
        logger.info(
            f"Tasks filtered: {serializer.data} with {date} and {content}")
        return Response(serializer.data)
