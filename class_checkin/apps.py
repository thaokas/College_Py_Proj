from django.apps import AppConfig
from pymilvus import MilvusClient
from insightface.app import FaceAnalysis

class ClassCheckinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'class_checkin'

    # def ready(self):
    #     global client, face_recognition
    #
    #     face_recognition.prepare(ctx_id=0, det_size=(640, 640))
    #
    #     # if client.has_collection(collection_name="all_face_database"):
    #     #     client.drop_collection(collection_name="all_face_database")
    #
    #     client.create_collection(
    #         collection_name="all_face_database",
    #         dimension=512
    #     )
