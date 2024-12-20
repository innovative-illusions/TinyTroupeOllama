from enum import Enum

class OpenAIEmbeddingModelType(Enum):
    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"
    TEXT_SIMILARITY_ADA_001 = "text-similarity-ada-001"
    TEXT_SEARCH_ADA_DOC_001 = "text-search-ada-doc-001"
    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    MXBAI_EMBED_LARGE = "mxbai-embed-large:latest"  # Add the custom model name here
