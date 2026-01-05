from fastapi import APIRouter



def health_router():
    router = APIRouter()

    @router.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return router
