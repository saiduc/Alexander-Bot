"""
This type stub file was generated by pyright.
"""

import logging
from collections import namedtuple
from .channel import *
from .raw_models import *
from .enums import Enum

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
class ListenerType(Enum):
    chunk = ...
    query_members = ...


Listener = namedtuple('Listener', ('type', 'future', 'predicate'))
log = logging.getLogger(__name__)
ReadyState = namedtuple('ReadyState', ('launch', 'guilds'))
class ConnectionState:
    def __init__(self, *, dispatch, chunker, handlers, syncer, http, loop, **options) -> None:
        ...
    
    def clear(self):
        ...
    
    def process_listeners(self, listener_type, argument, result):
        ...
    
    def call_handlers(self, key, *args, **kwargs):
        ...
    
    @property
    def self_id(self):
        ...
    
    @property
    def voice_clients(self):
        ...
    
    def store_user(self, data):
        ...
    
    def get_user(self, id):
        ...
    
    def store_emoji(self, guild, data):
        ...
    
    @property
    def guilds(self):
        ...
    
    @property
    def emojis(self):
        ...
    
    def get_emoji(self, emoji_id):
        ...
    
    @property
    def private_channels(self):
        ...
    
    def add_dm_channel(self, data):
        ...
    
    def chunks_needed(self, guild):
        ...
    
    async def request_offline_members(self, guilds):
        ...
    
    async def query_members(self, guild, query, limit, cache):
        ...
    
    def parse_ready(self, data):
        ...
    
    def parse_resumed(self, data):
        ...
    
    def parse_message_create(self, data):
        ...
    
    def parse_message_delete(self, data):
        ...
    
    def parse_message_delete_bulk(self, data):
        ...
    
    def parse_message_update(self, data):
        ...
    
    def parse_message_reaction_add(self, data):
        ...
    
    def parse_message_reaction_remove_all(self, data):
        ...
    
    def parse_message_reaction_remove(self, data):
        ...
    
    def parse_message_reaction_remove_emoji(self, data):
        ...
    
    def parse_presence_update(self, data):
        ...
    
    def parse_user_update(self, data):
        ...
    
    def parse_invite_create(self, data):
        ...
    
    def parse_invite_delete(self, data):
        ...
    
    def parse_channel_delete(self, data):
        ...
    
    def parse_channel_update(self, data):
        ...
    
    def parse_channel_create(self, data):
        ...
    
    def parse_channel_pins_update(self, data):
        ...
    
    def parse_channel_recipient_add(self, data):
        ...
    
    def parse_channel_recipient_remove(self, data):
        ...
    
    def parse_guild_member_add(self, data):
        ...
    
    def parse_guild_member_remove(self, data):
        ...
    
    def parse_guild_member_update(self, data):
        ...
    
    def parse_guild_emojis_update(self, data):
        ...
    
    def parse_guild_create(self, data):
        ...
    
    def parse_guild_sync(self, data):
        ...
    
    def parse_guild_update(self, data):
        ...
    
    def parse_guild_delete(self, data):
        ...
    
    def parse_guild_ban_add(self, data):
        ...
    
    def parse_guild_ban_remove(self, data):
        ...
    
    def parse_guild_role_create(self, data):
        ...
    
    def parse_guild_role_delete(self, data):
        ...
    
    def parse_guild_role_update(self, data):
        ...
    
    def parse_guild_members_chunk(self, data):
        ...
    
    def parse_guild_integrations_update(self, data):
        ...
    
    def parse_webhooks_update(self, data):
        ...
    
    def parse_voice_state_update(self, data):
        ...
    
    def parse_voice_server_update(self, data):
        ...
    
    def parse_typing_start(self, data):
        ...
    
    def parse_relationship_add(self, data):
        ...
    
    def parse_relationship_remove(self, data):
        ...
    
    def get_reaction_emoji(self, data):
        ...
    
    def get_channel(self, id):
        ...
    
    def create_message(self, *, channel, data):
        ...
    
    def receive_chunk(self, guild_id):
        ...
    
    def receive_member_query(self, guild_id, query):
        ...
    


class AutoShardedConnectionState(ConnectionState):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    async def request_offline_members(self, guilds, *, shard_id):
        ...
    
    def parse_ready(self, data):
        ...
    


