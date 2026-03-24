"""
Module for storing django choice fields for taxonomy models.
"""
from django.db import models


class UserGoal(models.TextChoices):
    """
    User goal choices, this will be used in skills quiz.
    """

    ChangeCareers = 'change_careers', 'I want to change careers'
    GetPromoted = 'get_promoted', 'I want to get promoted'
    ImproveCurrentRole = 'improve_current_role', 'I want to improve at my current role'
    Other = 'other', 'Other'


class ProductTypes(models.TextChoices):
    """
    Product types to be used in retrieving skills.
    """

    Course = 'course', 'Course'
    Program = 'program', 'Program'
    XBlock = 'xblock', 'XBlock'
    XBlockData = 'xblock_data', 'XBlockData'
