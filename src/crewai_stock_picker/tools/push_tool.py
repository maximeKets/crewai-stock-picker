from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests

class PushNotification(BaseModel):
    """A message to be sent to the user"""
    message: str = Field(..., description="The message to be sent to the user.")

