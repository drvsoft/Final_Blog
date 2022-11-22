from blog.models import Post

Post(title="Mi primer post", short_content="Es el primer post", content="Esto es el contenido del primer post que creamos").save()
Post(title="Mi segundo post", short_content="Es el segundo post", content="Esto es el contenido del segundo post que creamos").save()

print("Se cargo con éxito los post de pruebas")