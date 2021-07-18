import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template()
def index():
    return {}


@router.get('/register')
@template()
def register():
    return {}

