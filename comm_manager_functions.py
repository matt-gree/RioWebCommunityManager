import project_rio_lib.web_functions as web_func
import local_functions as loc_func
import data_parsing
from functools import partial
from project_rio_lib.web_caching import CompleterCache

class CommunityManagerBase:
    def __init__(self, cache: CompleterCache):
        self.cache = cache

        self.community_endpoints = {
            'Create Community': {
                'func': web_func.create_community,
                'inputs': [
                    'community_name_free',
                    'comm_type',
                    'private',
                    'global_link',
                    'comm_desc'
                ]
            },
            'Remove Members': {
                'unsupported': True
                # Endpoint is unecessary, use update_community
            },
            'Add Members': {
                'unsupported': True
                # Endpoint is unecessary, use invite_members
            },
            'Community Join': {
                'unsupported': True
                # Endpoint is not needed for a community admin
            },
            'Community Invite': {
                'func': web_func.community_invite,
                'inputs': [
                    'community_name_closed',
                    'invite_list'
                ]
            },
            'Community Members': {
                'func': web_func.community_members,
                'inputs': [
                    'community_name_closed'
                ],
                'parse_data': data_parsing.community_members_to_dataframe
            },
            'Community Tags': {
                'func': web_func.community_tags,
                'inputs': [
                    'community_name_closed'
                ],
                'parse_data': data_parsing.community_tags_to_dataframe
            },
            'Manage Community Bans': {
                'func': web_func.community_manage,
                'inputs': [
                    'community_name_closed',
                    'community_manage_bans',
                ]
            },
            'Remove Community Users': {
                'func': web_func.community_manage,
                'inputs': [
                    'community_name_closed',
                    'community_remove_users',
                ]
            },
            'Manage Community User Keys': {
                'func': web_func.community_manage,
                'inputs': [
                    'community_name_closed',
                    'manage_user_community_keys',
                ]
            },
            'Manage Community Admins': {
                'func': web_func.community_manage,
                'inputs': [
                    'community_name_closed',
                    'manage_community_admins',
                ]
            },
            'Get Community Sponsor': {
                'func': web_func.community_sponsor,
                'inputs': [
                    'community_name_closed',
                ],
                'fixed_inputs': {
                    'action': 'get'
                },
                'parse_data': data_parsing.print_community_sponsor
            },
            'Community-Wide User Keys': {
                'func': web_func.community_key,
                'inputs': [
                    'community_name_closed',
                    'key_action'
                ],
                'parse_data': data_parsing.community_user_keys_to_dataframe
            },
            'Create Component Tag': {
                'func': partial(web_func.create_tag, tag_type='Component'),
                'inputs': [
                    'community_name_closed',
                    'tag_name_free',
                    'tag_desc'
                ]
            },
            'Create Gecko Code Tag': {
                'func': partial(web_func.create_tag, tag_type='Gecko Code'),
                'inputs': [
                    'community_name_closed',
                    'tag_name_free',
                    'tag_desc',
                    'gecko_code',
                    'gecko_code_desc'
                ]
            },
            'Create Game Mode': {
                'func': web_func.create_game_mode,
                'inputs': [
                    'game_mode_name_free',
                    'game_mode_desc',
                    'game_mode_type',
                    'community_name_closed',
                    'start_date',
                    'end_date',
                    'add_tag_ids',
                    'game_mode_to_mirror_tags_from'
                ]
            },
            'Update Game Mode Name': {
                'func': web_func.update_game_mode,
                'inputs': [
                    'tag_set_id',
                    'game_mode_name_free'
                ]
            },
            'Update Game Mode Description': {
                'func': web_func.update_game_mode,
                'inputs': [
                    'tag_set_id',
                    'game_mode_description'
                ]
            },
            'Update Game Mode Type': {
                'func': web_func.update_game_mode,
                'inputs': [
                    'tag_set_id',
                    'game_mode_type'
                ]
            },
            'Add Tags to Game Mode': {
                'func': web_func.update_game_mode,
                'inputs': [
                    'tag_set_id',
                    'add_tag_ids'
                ]
            },
            'Remove Tags from Game Mode': {
                'func': web_func.update_game_mode,
                'inputs': [
                    'tag_set_id',
                    'remove_tag_ids'
                ]
            },
            'Update Game Mode End Date': {
                'func': web_func.update_game_mode,
                'inputs': [
                    'tag_set_id',
                    'end_date'
                ]
            },
            'Update Game Mode Start Date': {
                'func': web_func.update_game_mode,
                'inputs': [
                    'tag_set_id',
                    'start_date'
                ]
            },
            'List Game Mode Tags': {
                'func': web_func.list_game_mode_tags,
                'inputs': [
                    'tag_set_id'
                ],
                'parse_data': data_parsing.game_mode_tags_to_dataframe
            },
            'Show Game Mode Ladder': {
                'func': web_func.game_mode_ladder,
                'inputs': [
                    'game_mode_name_closed'
                ],
                'parse_data': data_parsing.ladder_to_dataframe
            },
            'Update Tag Name': {
                'func': web_func.update_tag,
                'inputs': [
                    'tag_id',
                    'tag_name_free'
                ]
            },
            'Update Tag Description': {
                'func': web_func.update_tag,
                'inputs': [
                    'tag_id',
                    'tag_desc'
                ]
            },
            'Update Tag Type': {
                'func': web_func.update_tag,
                'inputs': [
                    'tag_id',
                    'tag_type',
                ]
            },
            'Update Tag Gecko Code Desc': {
                'func': web_func.update_tag,
                'inputs': [
                    'tag_id',
                    'gecko_code_desc',
                ]
            },
            'Update Tag Gecko Code': {
                'func': web_func.update_tag,
                'inputs': [
                    'tag_id',
                    'gecko_code',
                ]
            },
            'Delete Game Mode': {
                'func': web_func.delete_game_mode,
                'inputs': [
                    'game_mode_name_closed'
                ]
            },
            'Delete Game': {
                'func': web_func.delete_game,
                'inputs': [
                    'game_id_dec'
                ]
            },
            'Manual Game Submission From Statfile': {
                'func': web_func.manual_game_submit,
                'inputs': [
                    'manual_submission_stat_file'
                ],
                'parse_data': data_parsing.print_data
            },
            'Tag Info': {
                'func': partial(loc_func.get_tag_info, tags_df=self.cache.return_tags_df()),
                'inputs': [
                    'tag_name_closed'
                ],
                'parse_data': data_parsing.print_df_columns_by_row
            },
            'Add Member to User Group': {
                'func': web_func.add_user_to_user_group,
                'inputs': [
                    'username',
                    'group_name'
                ],
                'parse_data': data_parsing.print_data
            },
            'Check Member in User Group': {
                'func': web_func.check_for_member_in_user_group,
                'inputs': [
                    'username',
                    'group_name'
                ],
                'parse_data': data_parsing.print_data
            }
        }
