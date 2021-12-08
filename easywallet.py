#!/.venv/bin python3
from src.parser import parse_args
from src.config import get_env_path

if __name__ == '__main__':
    env_path = get_env_path()
    args = parse_args()



