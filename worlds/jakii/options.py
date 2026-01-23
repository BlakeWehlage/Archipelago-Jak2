from dataclasses import dataclass
from functools import cached_property
from Options import PerGameCommonOptions, StartInventoryPool, Choice, Range, OptionCounter
from items import item_table


class CompletionCondition(Choice):
    """Set your goal for completion!"""
    display_name = "Completion Condition"
    option_complete_specific_mission = 1
    option_complete_number_of_missions = 2
    default = 1


class SpecificMissionForCompletion(Choice):
    """Set the specific mission to complete for the "Complete Specific Mission" completion condition."""
    display_name = "Specific Mission for Completion"
    option_unlock_mar_tomb = 40
    option_defeat_baron_at_palace = 22
    option_defeat_baron_in_tomb = 43
    option_defeat_metal_kor = 65
    default = 65


class NumberOfMissionsForCompletion(Range):
    """Set the number of missions to complete for the "Complete Number of Missions" completion condition."""
    display_name = "Number of Missions for Completion"
    range_start = 5
    range_end = 98
    default = 65


class TrapEffectDuration(Range):
    """The length of time, in seconds, of a trap's duration."""
    display_name= "Trap Effect Duration"
    range_start = 5
    range_end = 60
    default = 30


class TrapWeights(OptionCounter):
    """
    The list of traps and corresponding weights that will be randomly added to the item pool. A trap weight with 10 is
    twice as likely to appear as a trap with weight 5. Set a weight to 0 to prevent that trap from appearing altogether.
    If all weights are 0, no traps are created, overriding the values of "Percent of Filler Items Replaced with Traps".
    """
    display_name = "Trap Weights"
    min = 0
    default = {trap: 1 for trap in item_table(40-56)}
    valid_keys = sorted({trap for trap in item_table(40-56)})

    @cached_property
    def weights_pair(self) -> tuple[list[str], list[int]]:
        return list(self.value.keys()), list(self.value.values())

class PercentOfFillerReplacedWithTraps(Range):
    """
    The percentage of Filler Items that will be replaced with traps. This does not affect the number of progression
    items.

    If this value is greater than the number of filler items, then they will all be replaced with traps.
    """
    display_name = "Percent of Filler Items Replaced with Traps"
    range_start = 0
    range_end = 100
    default = 45

@dataclass
class JakIIOptions(PerGameCommonOptions):
    jak_2_completion_condition: CompletionCondition
    specific_mission_for_completion: SpecificMissionForCompletion
    number_of_missions_for_completion: NumberOfMissionsForCompletion
    trap_effect_duration: TrapEffectDuration
    trap_weights: TrapWeights
    percent_of_filler_items_replaced: PercentOfFillerReplacedWithTraps
    start_inventory_from_pool: StartInventoryPool