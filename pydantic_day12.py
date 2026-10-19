from pydantic import BaseModel, EmailStr, Field

class UserConfig(BaseModel):
    user_id: int
    email: EmailStr
    is_active: bool = True
    tags: list[str] = Field(default_factory=list)

# Data parsing & coercion handled in Rust core
raw_data = {"user_id": "1001", "email": "dev@example.com", "tags": ["admin"]}
user = UserConfig(**raw_data)

print(f"Parsed ID Type: {type(user.user_id)}") # <class 'int'>
print(user.model_dump_json())