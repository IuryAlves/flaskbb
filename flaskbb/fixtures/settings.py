# -*- coding: utf-8 -*-
"""
    flaskbb.fixtures.settings
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    The fixtures module for our settings.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from flask_themes2 import get_themes_list

from flaskbb.extensions import babel


def available_themes():
    return [(theme.identifier, theme.name) for theme in get_themes_list()]


def available_markups():
    return [('bbcode', 'BBCode'), ('markdown', 'Markdown')]


def available_languages():
    return [(locale.language, locale.display_name)
            for locale in babel.list_translations()]


fixture = (
    # Settings Group
    ('general', {
        'name': "General Settings",
        'description': "How many items per page are displayed.",
        'settings': (
            ('project_title', {
                'value':        "FlaskBB",
                'value_type':   "string",
                'name':         "Project title",
                'description':  "The title of the project.",
            }),
            ('project_subtitle', {
                'value':        "A lightweight forum software in Flask",
                'value_type':   "string",
                'name':         "Project subtitle",
                'description':  "A short description of the project.",
            }),
            ('posts_per_page', {
                'value':        10,
                'value_type':   "integer",
                'extra':        {'min': 5},
                'name':         "Posts per page",
                'description':  "Number of posts displayed per page.",
            }),
            ('topics_per_page', {
                'value':        10,
                'value_type':   "integer",
                'extra':        {'min': 5},
                'name':         "Topics per page",
                'description':  "Number of topics displayed per page.",
            }),
            ('users_per_page', {
                'value':        10,
                'value_type':   "integer",
                'extra':        {'min': 5},
                'name':         "Users per page",
                'description':  "Number of users displayed per page.",
            }),
        ),
    }),
    ('misc', {
        'name': "Misc Settings",
        'description': "Miscellaneous settings.",
        'settings': (
            ('online_last_minutes', {
                'value':        15,
                'value_type':   "integer",
                'extra':        {'min': 0},
                'name':         "Online last minutes",
                'description':  "How long a user can be inactive before he is marked as offline. 0 to disable it.",
            }),
            ('title_length', {
                'value':        15,
                'value_type':   "integer",
                'extra':        {'min': 0},
                'name':         "Topic title length",
                'description':  "The length of the topic title shown on the index."
            }),
            ('tracker_length', {
                'value':        7,
                'value_type':   "integer",
                'extra':        {'min': 0},
                'name':         "Tracker length",
                'description':  "The days for how long the forum should deal with unread topics. 0 to disable it."
            }),
            ('markup_type', {
                'value':        "bbcode",
                'value_type':   "select",
                'extra':        {'choices': available_markups},
                'name':         "Post markup",
                'description':  "Select post markup type."
            })
        ),
    }),
    ('appearance', {
        'name': "Appearance Settings",
        "description": "Change the theme and language for your forum.",
        "settings": (
            ('default_theme', {
                'value':        "bootstrap3",
                'value_type':   "select",
                'extra':        {'choices': available_themes},
                'name':         "Default Theme",
                'description':  "Change the default theme for your forum."
            }),
            ('default_language', {
                'value':        "en",
                'value_type':   "select",
                'extra':        {'choices': available_languages},
                'name':         "Default Language",
                'description':  "Change the default language for your forum."
            }),
        ),
    }),
)
