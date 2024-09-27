from contextvars import ContextVar
from fastapi_babel import Babel
from fastapi_babel import BabelConfigs
from fastapi_babel import _

configs = BabelConfigs(
    ROOT_DIR=__file__,
    BABEL_DEFAULT_LOCALE="en",
    BABEL_TRANSLATION_DIRECTORY="lang",
)

babel: Babel = Babel(configs=configs)

def _(message: str) -> str:
    return babel.gettext(message)


if __name__ == "__main__":
    babel.run_cli()
