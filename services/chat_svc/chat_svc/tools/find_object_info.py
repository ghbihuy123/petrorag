from langchain.tools import tool
import pandas as pd
from difflib import SequenceMatcher
from chat_svc.settings import common_config

@tool('search_tool')
def find_object_info(object_type_name: str) -> str:
    """
    Tìm kiếm mã object type của tên sản phẩm với khả năng tìm kiếm linh hoạt

    Ví dụ: tìm cho tôi mã object type của máy nén khí
    Suy ra: object_type_name = "máy nén khí"
    
    Hỗ trợ:
    - Tìm kiếm không phân biệt hoa thường
    - Tìm kiếm gần đúng (fuzzy matching)
    - Tìm kiếm theo từng từ riêng lẻ
    - Tìm kiếm độc lập với thứ tự từ

    Args:
        object_type_name: Search terms to look for
    """
    df = pd.read_excel(
        common_config.object_type_db_path,
        sheet_name='OBject Type'
    )

    search_term = object_type_name.lower().strip()
    
    # 1. Try exact match (case-insensitive)
    exact_mask = df['Object type text'].str.lower() == search_term
    if exact_mask.any():
        return str(df[exact_mask]['ObjectType'].iloc[0])
    
    # 2. Try word-order-independent match with word set comparison
    search_words = set(search_term.split())
    
    def contains_all_words(text):
        if pd.isna(text):
            return False
        text_words = set(text.lower().split())
        return search_words.issubset(text_words)
    
    word_match_mask = df['Object type text'].apply(contains_all_words)
    if word_match_mask.any():
        # If multiple matches with same words, return the best similarity match
        matches = df[word_match_mask].copy()
        matches['similarity'] = matches['Object type text'].apply(
            lambda x: SequenceMatcher(None, search_term, x.lower()).ratio()
        )
        best_match = matches.loc[matches['similarity'].idxmax()]
        return str(best_match['ObjectType'])
    
    # 3. Fuzzy matching - find best similarity match
    def similarity_score(text):
        if pd.isna(text):
            return 0
        return SequenceMatcher(None, search_term, text.lower()).ratio()
    
    scores = df['Object type text'].apply(similarity_score)
    best_match_idx = scores.idxmax()
    best_score = scores[best_match_idx]
    
    # If best match has reasonable similarity (>60%), return it
    if best_score > 0.6:
        return str(df.loc[best_match_idx, 'ObjectType'])
    
    # If no good match found
    return f"Object type '{object_type_name}' not found. Best match was '{df.loc[best_match_idx, 'Object type text']}' with {best_score*100:.1f}% similarity"