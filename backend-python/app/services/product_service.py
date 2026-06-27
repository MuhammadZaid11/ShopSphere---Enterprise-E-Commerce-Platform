import orjson

from app.redis_client import redis_client
from app.repositories.product_repository import ProductRepository
from app.models.product import Product


class ProductService:

    CACHE_KEY = "products"

    @staticmethod
    def get_products(db):

        cached = redis_client.get(ProductService.CACHE_KEY)

        if cached:
            print("✅ Cache Hit")
            return orjson.loads(cached)

        print("❌ Cache Miss")

        products = ProductRepository.get_all(db)

        result = [
            {
                "id": p.id,
                "name": p.name,
                "description": p.description,
                "category": p.category,
                "price": p.price,
                "stock": p.stock
            }
            for p in products
        ]

        redis_client.set(
            ProductService.CACHE_KEY,
            orjson.dumps(result),
            ex=60
        )

        return result

    @staticmethod
    def create_product(db, product_schema):

        product = Product(**product_schema.model_dump())

        product = ProductRepository.create(db, product)

        redis_client.delete(ProductService.CACHE_KEY)

        return product