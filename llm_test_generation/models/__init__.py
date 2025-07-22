from enum import Enum
from pathlib import Path

# 레지스트리 모듈 등록
from llm_test_generation.models.openai.response import Response

# 레지스트리 이름 등록
class Available_Model(Enum):
  Response = "response"