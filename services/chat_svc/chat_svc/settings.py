from pydantic_settings import BaseSettings, SettingsConfigDict

class CommonConfig(BaseSettings):
    object_type_db_path: str = './chat_svc/data/DanhMuc_ObjectType.xlsx'
    common_question_db_path: str = './chat_svc/data/common_question.xlsx'

    openai_key: str = 'skt-t1'    

    model_config = SettingsConfigDict(
        case_sensitive=False
    )

common_config = CommonConfig()