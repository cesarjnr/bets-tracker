from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from django.http import HttpResponse
from bets_tracker.settings import BET365_API_TOKEN
import undetected_chromedriver.v2 as uc
import pandas as pd
import requests
import time
import json

events = [
    {
        "id": "130404835",
        "sport_id": "18",
        "time": "1672359000",
        "time_status": "0",
        "league": {
            "id": "10041830",
            "name": "NBA"
        },
        "home": {
            "id": "10400349",
            "name": "OKC Thunder"
        },
        "away": {
            "id": "10400347",
            "name": "CHA Hornets"
        },
        "ss": None,
        "our_event_id": "5816607",
        "r_id": None,
        "updated_at": "1672325844"
    },
    # {
    #     "id": "130404838",
    #     "sport_id": "18",
    #     "time": "1672359000",
    #     "time_status": "0",
    #     "league": {
    #         "id": "10041830",
    #         "name": "NBA"
    #     },
    #     "home": {
    #         "id": "10363389",
    #         "name": "CLE Cavaliers"
    #     },
    #     "away": {
    #         "id": "10402330",
    #         "name": "IND Pacers"
    #     },
    #     "ss": None,
    #     "our_event_id": "5821475",
    #     "r_id": None,
    #     "updated_at": "1672325843"
    # },
    # {
    #     "id": "130404841",
    #     "sport_id": "18",
    #     "time": "1672360800",
    #     "time_status": "0",
    #     "league": {
    #         "id": "10041830",
    #         "name": "NBA"
    #     },
    #     "home": {
    #         "id": "10362528",
    #         "name": "LA Clippers"
    #     },
    #     "away": {
    #         "id": "10363390",
    #         "name": "BOS Celtics"
    #     },
    #     "ss": None,
    #     "our_event_id": "5829167",
    #     "r_id": None,
    #     "updated_at": "1672325844"
    # },
    # {
    #     "id": "130404844",
    #     "sport_id": "18",
    #     "time": "1672360800",
    #     "time_status": "0",
    #     "league": {
    #         "id": "10041830",
    #         "name": "NBA"
    #     },
    #     "home": {
    #         "id": "10400348",
    #         "name": "MEM Grizzlies"
    #     },
    #     "away": {
    #         "id": "10362526",
    #         "name": "TOR Raptors"
    #     },
    #     "ss": None,
    #     "our_event_id": "5803570",
    #     "r_id": None,
    #     "updated_at": "1672325844"
    # },
    # {
    #     "id": "130404847",
    #     "sport_id": "18",
    #     "time": "1672362600",
    #     "time_status": "0",
    #     "league": {
    #         "id": "10041830",
    #         "name": "NBA"
    #     },
    #     "home": {
    #         "id": "10406469",
    #         "name": "NY Knicks"
    #     },
    #     "away": {
    #         "id": "10363392",
    #         "name": "SA Spurs"
    #     },
    #     "ss": None,
    #     "our_event_id": "5812456",
    #     "r_id": None,
    #     "updated_at": "1672325844"
    # },
    # {
    #     "id": "130404850",
    #     "sport_id": "18",
    #     "time": "1672364400",
    #     "time_status": "0",
    #     "league": {
    #         "id": "10041830",
    #         "name": "NBA"
    #     },
    #     "home": {
    #         "id": "10406470",
    #         "name": "HOU Rockets"
    #     },
    #     "away": {
    #         "id": "10400350",
    #         "name": "DAL Mavericks"
    #     },
    #     "ss": None,
    #     "our_event_id": "5812455",
    #     "r_id": None,
    #     "updated_at": "1672325844"
    # }
]
odds = {
    "FI": "130404835",
    "event_id": "5816607",
    "half_props": {
        "updated_at": "1672326032",
        "key": "#AC#B18#C20604387#D19#E15942762#F19#I4#",
        "sp": {
            "1st_half_team_totals": {
                "id": "181159",
                "name": "1st Half Team Totals",
                "odds": [
                    {
                        "id": "2056370853",
                        "odds": "1.86",
                        "header": "1",
                        "handicap": "Over 61.5"
                    },
                    {
                        "id": "2056370854",
                        "odds": "1.86",
                        "header": "1",
                        "handicap": "Under 61.5"
                    },
                    {
                        "id": "2056370877",
                        "odds": "1.86",
                        "header": "2",
                        "handicap": "Over 61.5"
                    },
                    {
                        "id": "2056370878",
                        "odds": "1.86",
                        "header": "2",
                        "handicap": "Under 61.5"
                    }
                ]
            },
            "alternative_1st_half_team_totals": {
                "id": "181160",
                "name": "Alternative 1st Half Team Totals",
                "odds": []
            },
            "alternative_1st_half_point_spread": {
                "id": "181137",
                "name": "Alternative 1st Half Point Spread",
                "odds": []
            },
            "alternative_1st_half_totals": {
                "id": "181148",
                "name": "Alternative 1st Half Totals",
                "odds": []
            },
            "1st_half_winning_margin": {
                "id": "181185",
                "name": "1st Half Winning Margin",
                "odds": [
                    {
                        "id": "2056370916",
                        "odds": "6.50",
                        "header": "1",
                        "name": "1-3"
                    },
                    {
                        "id": "2056370917",
                        "odds": "7.50",
                        "header": "1",
                        "name": "4-6"
                    },
                    {
                        "id": "2056370918",
                        "odds": "9.00",
                        "header": "1",
                        "name": "7-9"
                    },
                    {
                        "id": "2056370919",
                        "odds": "12.00",
                        "header": "1",
                        "name": "10-12"
                    },
                    {
                        "id": "2056370920",
                        "odds": "19.00",
                        "header": "1",
                        "name": "13-15"
                    },
                    {
                        "id": "2056370922",
                        "odds": "15.00",
                        "header": "1",
                        "name": "16+"
                    },
                    {
                        "id": "2056370924",
                        "odds": "6.50",
                        "header": "2",
                        "name": "1-3"
                    },
                    {
                        "id": "2056370925",
                        "odds": "7.00",
                        "header": "2",
                        "name": "4-6"
                    },
                    {
                        "id": "2056370926",
                        "odds": "9.00",
                        "header": "2",
                        "name": "7-9"
                    },
                    {
                        "id": "2056370927",
                        "odds": "12.00",
                        "header": "2",
                        "name": "10-12"
                    },
                    {
                        "id": "2056370928",
                        "odds": "19.00",
                        "header": "2",
                        "name": "13-15"
                    },
                    {
                        "id": "2056370929",
                        "odds": "15.00",
                        "header": "2",
                        "name": "16+"
                    },
                    {
                        "id": "2056370930",
                        "odds": "15.00",
                        "name": "Tie"
                    }
                ]
            },
            "1st_half_result_and_total": {
                "id": "181181",
                "name": "1st Half Result and Total",
                "odds": [
                    {
                        "id": "2056370901",
                        "odds": "3.75",
                        "header": "Over",
                        "name": "1",
                        "handicap": "122.5"
                    },
                    {
                        "id": "2056370903",
                        "odds": "3.75",
                        "header": "Over",
                        "name": "2",
                        "handicap": "122.5"
                    },
                    {
                        "id": "2056370905",
                        "odds": "26.00",
                        "header": "Over",
                        "name": "Tie",
                        "handicap": "122.5"
                    },
                    {
                        "id": "2056370902",
                        "odds": "3.75",
                        "header": "Under",
                        "name": "1",
                        "handicap": "122.5"
                    },
                    {
                        "id": "2056370904",
                        "odds": "3.75",
                        "header": "Under",
                        "name": "2",
                        "handicap": "122.5"
                    },
                    {
                        "id": "2056370906",
                        "odds": "26.00",
                        "header": "Under",
                        "name": "Tie",
                        "handicap": "122.5"
                    }
                ]
            },
            "1st_half_handicap_and_total": {
                "id": "181182",
                "name": "1st Half Handicap and Total",
                "odds": [
                    {
                        "id": "2057882998",
                        "odds": "3.50",
                        "name": "OKC Thunder +0.5 & Over 122.5"
                    },
                    {
                        "id": "2057883000",
                        "odds": "3.60",
                        "name": "CHA Hornets -0.5 & Over 122.5"
                    },
                    {
                        "id": "2057882999",
                        "odds": "3.50",
                        "name": "OKC Thunder +0.5 & Under 122.5"
                    },
                    {
                        "id": "2057883001",
                        "odds": "3.60",
                        "name": "CHA Hornets -0.5 & Under 122.5"
                    }
                ]
            },
            "1st_half_race_to_(points)": {
                "id": "181186",
                "name": "1st Half Race to (Points)",
                "odds": [
                    {
                        "id": "2056370931",
                        "odds": "1.83",
                        "header": "1",
                        "name": "20"
                    },
                    {
                        "id": "2056370934",
                        "odds": "1.83",
                        "header": "1",
                        "name": "25"
                    },
                    {
                        "id": "2056370937",
                        "odds": "1.83",
                        "header": "1",
                        "name": "30"
                    },
                    {
                        "id": "2056370940",
                        "odds": "1.83",
                        "header": "1",
                        "name": "35"
                    },
                    {
                        "id": "2056370943",
                        "odds": "1.83",
                        "header": "1",
                        "name": "40"
                    },
                    {
                        "id": "2056370948",
                        "odds": "1.83",
                        "header": "1",
                        "name": "45"
                    },
                    {
                        "id": "2056370951",
                        "odds": "1.83",
                        "header": "1",
                        "name": "50"
                    },
                    {
                        "id": "2056370954",
                        "odds": "1.90",
                        "header": "1",
                        "name": "55"
                    },
                    {
                        "id": "2056370957",
                        "odds": "2.25",
                        "header": "1",
                        "name": "60"
                    },
                    {
                        "id": "2056370932",
                        "odds": "1.83",
                        "header": "2",
                        "name": "20"
                    },
                    {
                        "id": "2056370935",
                        "odds": "1.83",
                        "header": "2",
                        "name": "25"
                    },
                    {
                        "id": "2056370938",
                        "odds": "1.83",
                        "header": "2",
                        "name": "30"
                    },
                    {
                        "id": "2056370941",
                        "odds": "1.83",
                        "header": "2",
                        "name": "35"
                    },
                    {
                        "id": "2056370945",
                        "odds": "1.83",
                        "header": "2",
                        "name": "40"
                    },
                    {
                        "id": "2056370949",
                        "odds": "1.83",
                        "header": "2",
                        "name": "45"
                    },
                    {
                        "id": "2056370952",
                        "odds": "1.83",
                        "header": "2",
                        "name": "50"
                    },
                    {
                        "id": "2056370955",
                        "odds": "1.90",
                        "header": "2",
                        "name": "55"
                    },
                    {
                        "id": "2056370958",
                        "odds": "2.20",
                        "header": "2",
                        "name": "60"
                    },
                    {
                        "id": "2056370933",
                        "odds": "101.00",
                        "header": "Neither",
                        "name": "20"
                    },
                    {
                        "id": "2056370936",
                        "odds": "101.00",
                        "header": "Neither",
                        "name": "25"
                    },
                    {
                        "id": "2056370939",
                        "odds": "101.00",
                        "header": "Neither",
                        "name": "30"
                    },
                    {
                        "id": "2056370942",
                        "odds": "101.00",
                        "header": "Neither",
                        "name": "35"
                    },
                    {
                        "id": "2056370946",
                        "odds": "101.00",
                        "header": "Neither",
                        "name": "40"
                    },
                    {
                        "id": "2056370950",
                        "odds": "81.00",
                        "header": "Neither",
                        "name": "45"
                    },
                    {
                        "id": "2056370953",
                        "odds": "31.00",
                        "header": "Neither",
                        "name": "50"
                    },
                    {
                        "id": "2056370956",
                        "odds": "15.00",
                        "header": "Neither",
                        "name": "55"
                    },
                    {
                        "id": "2056370959",
                        "odds": "4.75",
                        "header": "Neither",
                        "name": "60"
                    }
                ]
            },
            "1st_half_both_teams_to_score_x_points": {
                "id": "181195",
                "name": "1st Half Both Teams to Score X Points",
                "odds": [
                    {
                        "id": "2056370966",
                        "odds": "1.01",
                        "header": "Yes",
                        "name": "40"
                    },
                    {
                        "id": "2056370967",
                        "odds": "18.00",
                        "header": "No",
                        "name": "40"
                    }
                ]
            },
            "1st_half_team_to_score_x_points": {
                "id": "181198",
                "name": "1st Half Team to Score X Points",
                "odds": [
                    {
                        "id": "2056370972",
                        "odds": "1.08",
                        "header": "Yes",
                        "name": "50",
                        "team": "1"
                    },
                    {
                        "id": "2056370973",
                        "odds": "8.25",
                        "header": "No",
                        "name": "50",
                        "team": "1"
                    },
                    {
                        "id": "2056370978",
                        "odds": "1.08",
                        "header": "Yes",
                        "name": "50",
                        "team": "2"
                    },
                    {
                        "id": "2056370979",
                        "odds": "8.25",
                        "header": "No",
                        "name": "50",
                        "team": "2"
                    }
                ]
            },
            "1st_half_spread_3_way": {
                "id": "181147",
                "name": "1st Half Spread 3-Way",
                "odds": [
                    {
                        "id": "2056370827",
                        "odds": "2.10",
                        "header": "1",
                        "handicap": "-1.0"
                    },
                    {
                        "id": "2056370828",
                        "odds": "17.00",
                        "header": "Tie",
                        "handicap": "+1.0"
                    },
                    {
                        "id": "2056370829",
                        "odds": "1.80",
                        "header": "2",
                        "handicap": "+1.0"
                    }
                ]
            },
            "1st_half_totals_3_way": {
                "id": "181158",
                "name": "1st Half Totals 3-Way",
                "odds": [
                    {
                        "id": "2056370850",
                        "odds": "1.90",
                        "header": "Over",
                        "name": "123.0"
                    },
                    {
                        "id": "2056370851",
                        "odds": "23.00",
                        "header": "Exactly",
                        "name": "123.0"
                    },
                    {
                        "id": "2056370852",
                        "odds": "1.90",
                        "header": "Under",
                        "name": "123.0"
                    }
                ]
            },
            "1st_half_money_line_3_way": {
                "id": "181183",
                "name": "1st Half Money Line 3-Way",
                "odds": [
                    {
                        "id": "2056370911",
                        "odds": "2.00",
                        "name": "1"
                    },
                    {
                        "id": "2056370912",
                        "odds": "15.00",
                        "name": "Tie"
                    },
                    {
                        "id": "2056370913",
                        "odds": "1.90",
                        "name": "2"
                    }
                ]
            },
            "1st_half_double_chance": {
                "id": "181184",
                "name": "1st Half Double Chance",
                "odds": []
            },
            "1st_half_total_odd_even": {
                "id": "181204",
                "name": "1st Half Total Odd\/Even",
                "odds": []
            }
        }
    },
    "main": {
        "updated_at": "1672325778",
        "key": "#AC#B18#C20604387#D19#E15942762#F19#",
        "sp": {
            "game_lines": {
                "id": "1453",
                "name": "Game Lines",
                "odds": [
                    {
                        "id": "2049434755",
                        "odds": "1.90",
                        "header": "1",
                        "name": "Spread",
                        "handicap": "+1.0"
                    },
                    {
                        "id": "2049434762",
                        "odds": "1.90",
                        "header": "1",
                        "name": "Total",
                        "handicap": "O 239.0"
                    },
                    {
                        "id": "2049434758",
                        "odds": "2.00",
                        "header": "1",
                        "name": "Money Line"
                    },
                    {
                        "id": "2049434756",
                        "odds": "1.90",
                        "header": "2",
                        "name": "Spread",
                        "handicap": "-1.0"
                    },
                    {
                        "id": "2049434764",
                        "odds": "1.90",
                        "header": "2",
                        "name": "Total",
                        "handicap": "U 239.0"
                    },
                    {
                        "id": "2049434760",
                        "odds": "1.83",
                        "header": "2",
                        "name": "Money Line"
                    }
                ]
            },
            "1st_half": {
                "id": "928",
                "name": "1st Half",
                "odds": [
                    {
                        "id": "2056370665",
                        "odds": "1.86",
                        "header": "1",
                        "name": "Spread",
                        "handicap": "+0.5"
                    },
                    {
                        "id": "2056370633",
                        "odds": "1.90",
                        "header": "1",
                        "name": "Total",
                        "handicap": "O 122.5"
                    },
                    {
                        "id": "2056370686",
                        "odds": "1.95",
                        "header": "1",
                        "name": "Money Line"
                    },
                    {
                        "id": "2056370666",
                        "odds": "1.95",
                        "header": "2",
                        "name": "Spread",
                        "handicap": "-0.5"
                    },
                    {
                        "id": "2056370634",
                        "odds": "1.90",
                        "header": "2",
                        "name": "Total",
                        "handicap": "U 122.5"
                    },
                    {
                        "id": "2056370687",
                        "odds": "1.86",
                        "header": "2",
                        "name": "Money Line"
                    }
                ]
            },
            "1st_quarter": {
                "id": "941",
                "name": "1st Quarter",
                "odds": [
                    {
                        "id": "2056370637",
                        "odds": "1.83",
                        "header": "1",
                        "name": "Spread",
                        "handicap": "+0.5"
                    },
                    {
                        "id": "2056370639",
                        "odds": "1.90",
                        "header": "1",
                        "name": "Total",
                        "handicap": "O 61.5"
                    },
                    {
                        "id": "2056370690",
                        "odds": "1.90",
                        "header": "1",
                        "name": "Money Line"
                    },
                    {
                        "id": "2056370638",
                        "odds": "2.00",
                        "header": "2",
                        "name": "Spread",
                        "handicap": "-0.5"
                    },
                    {
                        "id": "2056370640",
                        "odds": "1.90",
                        "header": "2",
                        "name": "Total",
                        "handicap": "U 61.5"
                    },
                    {
                        "id": "2056370691",
                        "odds": "1.90",
                        "header": "2",
                        "name": "Money Line"
                    }
                ]
            },
            "okc_thunder_@_cha_hornets": {
                "id": 0,
                "name": "OKC Thunder @ CHA Hornets",
                "odds": []
            }
        }
    },
    "main_props": {
        "updated_at": "1672326025",
        "key": "#AC#B18#C20604387#D19#E15942762#F19#I1#",
        "sp": {
            "alternative_point_spread": {
                "id": "181285",
                "name": "Alternative Point Spread",
                "odds": []
            },
            "alternative_game_total": {
                "id": "181286",
                "name": "Alternative Game Total",
                "odds": []
            },
            "alternative_point_spread_2": {
                "id": "180968",
                "name": "Alternative Point Spread 2",
                "odds": []
            },
            "alternative_game_total_2": {
                "id": "180979",
                "name": "Alternative Game Total 2",
                "odds": []
            },
            "result_and_both_teams_to_score_'x'_points": {
                "id": "181273",
                "name": "Result and Both Teams to Score 'X' Points",
                "odds": [
                    {
                        "id": "2056372351",
                        "odds": "2.15",
                        "header": "100",
                        "name": "OKC Thunder and Yes"
                    },
                    {
                        "id": "2056372356",
                        "odds": "13.00",
                        "header": "100",
                        "name": "OKC Thunder and No"
                    },
                    {
                        "id": "2056372359",
                        "odds": "2.00",
                        "header": "100",
                        "name": "CHA Hornets and Yes"
                    },
                    {
                        "id": "2056372361",
                        "odds": "12.00",
                        "header": "100",
                        "name": "CHA Hornets and No"
                    },
                    {
                        "id": "2056372367",
                        "odds": "6.00",
                        "header": "120",
                        "name": "OKC Thunder and Yes"
                    },
                    {
                        "id": "2056372369",
                        "odds": "2.65",
                        "header": "120",
                        "name": "OKC Thunder and No"
                    },
                    {
                        "id": "2056372370",
                        "odds": "5.50",
                        "header": "120",
                        "name": "CHA Hornets and Yes"
                    },
                    {
                        "id": "2056372371",
                        "odds": "2.50",
                        "header": "120",
                        "name": "CHA Hornets and No"
                    }
                ]
            },
            "double_result": {
                "id": "1517",
                "name": "Double Result",
                "odds": [
                    {
                        "id": "2056370677",
                        "odds": "2.75",
                        "name": "OKC Thunder - OKC Thunder"
                    },
                    {
                        "id": "2056370678",
                        "odds": "26.00",
                        "name": "Tie - OKC Thunder"
                    },
                    {
                        "id": "2056370679",
                        "odds": "6.50",
                        "name": "CHA Hornets - OKC Thunder"
                    },
                    {
                        "id": "2056370680",
                        "odds": "6.50",
                        "name": "OKC Thunder - CHA Hornets"
                    },
                    {
                        "id": "2056370681",
                        "odds": "23.00",
                        "name": "Tie - CHA Hornets"
                    },
                    {
                        "id": "2056370682",
                        "odds": "2.55",
                        "name": "CHA Hornets - CHA Hornets"
                    }
                ]
            },
            "match_result_and_total": {
                "id": "181125",
                "name": "Match Result and Total",
                "odds": [
                    {
                        "id": "2056370787",
                        "odds": "3.75",
                        "header": "1",
                        "handicap": "Over 239.5"
                    },
                    {
                        "id": "2056370788",
                        "odds": "3.60",
                        "header": "1",
                        "handicap": "Under 239.5"
                    },
                    {
                        "id": "2056370789",
                        "odds": "3.50",
                        "header": "2",
                        "handicap": "Over 239.5"
                    },
                    {
                        "id": "2056370790",
                        "odds": "3.40",
                        "header": "2",
                        "handicap": "Under 239.5"
                    }
                ]
            },
            "match_handicap_and_total": {
                "id": "181126",
                "name": "Match Handicap and Total",
                "odds": [
                    {
                        "id": "2057602317",
                        "odds": "3.60",
                        "name": "OKC Thunder +0.5 & Over 239.5"
                    },
                    {
                        "id": "2057602319",
                        "odds": "3.60",
                        "name": "CHA Hornets -0.5 & Over 239.5"
                    },
                    {
                        "id": "2057602318",
                        "odds": "3.50",
                        "name": "OKC Thunder +0.5 & Under 239.5"
                    },
                    {
                        "id": "2057602332",
                        "odds": "3.50",
                        "name": "CHA Hornets -0.5 & Under 239.5"
                    }
                ]
            },
            "winning_margin": {
                "id": "1518",
                "name": "Winning Margin",
                "odds": [
                    {
                        "id": "2056370647",
                        "odds": "12.00",
                        "header": "1",
                        "name": "1-2"
                    },
                    {
                        "id": "2056370648",
                        "odds": "7.00",
                        "header": "1",
                        "name": "3-6"
                    },
                    {
                        "id": "2056370649",
                        "odds": "10.00",
                        "header": "1",
                        "name": "7-9"
                    },
                    {
                        "id": "2056370650",
                        "odds": "10.00",
                        "header": "1",
                        "name": "10-13"
                    },
                    {
                        "id": "2056370651",
                        "odds": "17.00",
                        "header": "1",
                        "name": "14-16"
                    },
                    {
                        "id": "2056370652",
                        "odds": "17.00",
                        "header": "1",
                        "name": "17-20"
                    },
                    {
                        "id": "2056370653",
                        "odds": "8.50",
                        "header": "1",
                        "name": "21+"
                    },
                    {
                        "id": "2056370654",
                        "odds": "12.00",
                        "header": "2",
                        "name": "1-2"
                    },
                    {
                        "id": "2056370655",
                        "odds": "7.00",
                        "header": "2",
                        "name": "3-6"
                    },
                    {
                        "id": "2056370656",
                        "odds": "10.00",
                        "header": "2",
                        "name": "7-9"
                    },
                    {
                        "id": "2056370657",
                        "odds": "9.50",
                        "header": "2",
                        "name": "10-13"
                    },
                    {
                        "id": "2056370658",
                        "odds": "15.00",
                        "header": "2",
                        "name": "14-16"
                    },
                    {
                        "id": "2056370659",
                        "odds": "17.00",
                        "header": "2",
                        "name": "17-20"
                    },
                    {
                        "id": "2056370660",
                        "odds": "8.25",
                        "header": "2",
                        "name": "21+"
                    }
                ]
            },
            "winning_margin_3_way": {
                "id": "180163",
                "name": "Winning Margin 3-Way",
                "odds": []
            },
            "winning_margin_7_way": {
                "id": "180164",
                "name": "Winning Margin 7-Way",
                "odds": []
            },
            "winning_margin_12_way": {
                "id": "180165",
                "name": "Winning Margin 12-Way",
                "odds": []
            },
            "race_to_20_points": {
                "id": "1503",
                "name": "Race to 20 Points",
                "odds": [
                    {
                        "id": "2056370675",
                        "odds": "1.86",
                        "name": "1"
                    },
                    {
                        "id": "2056370676",
                        "odds": "1.86",
                        "name": "2"
                    }
                ]
            },
            "tied_at_end_of_regulation?": {
                "id": "181127",
                "name": "Tied at End Of Regulation?",
                "odds": []
            },
            "quarter_correct_score": {
                "id": "181276",
                "name": "Quarter Correct Score",
                "odds": []
            },
            "highest_scoring_half": {
                "id": "181131",
                "name": "Highest Scoring Half",
                "odds": []
            },
            "game_total_(bands)_8_way": {
                "id": "181001",
                "name": "Game Total (Bands) 8-Way",
                "odds": []
            },
            "game_total_(bands)_3_way": {
                "id": "180999",
                "name": "Game Total (Bands) 3-Way",
                "odds": []
            },
            "game_total_odd_even": {
                "id": "180013",
                "name": "Game Total - Odd\/Even",
                "odds": []
            }
        }
    },
    "others": [
        {
            "updated_at": "1672325987",
            "sp": {
                "game_total_odd_even": {
                    "id": "180013",
                    "name": "Game Total - Odd\/Even",
                    "odds": [
                        {
                            "id": "2056370698",
                            "odds": "1.90",
                            "name": "Odd"
                        },
                        {
                            "id": "2056370699",
                            "odds": "1.90",
                            "name": "Even"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325853",
            "sp": {
                "winning_margin_3_way": {
                    "id": "180163",
                    "name": "Winning Margin 3-Way",
                    "odds": [
                        {
                            "id": "2056370700",
                            "odds": "2.70",
                            "header": "1",
                            "name": "6 or more"
                        },
                        {
                            "id": "2056370708",
                            "odds": "2.55",
                            "header": "2",
                            "name": "6 or more"
                        },
                        {
                            "id": "2056370709",
                            "odds": "3.00",
                            "name": "Any Other Result"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326033",
            "sp": {
                "winning_margin_7_way": {
                    "id": "180164",
                    "name": "Winning Margin 7-Way",
                    "odds": [
                        {
                            "id": "2056370710",
                            "odds": "3.00",
                            "name": "1-5"
                        },
                        {
                            "id": "2056370711",
                            "odds": "3.50",
                            "name": "6-10"
                        },
                        {
                            "id": "2056370712",
                            "odds": "4.75",
                            "name": "11-15"
                        },
                        {
                            "id": "2056370713",
                            "odds": "7.50",
                            "name": "16-20"
                        },
                        {
                            "id": "2056370714",
                            "odds": "11.00",
                            "name": "21-25"
                        },
                        {
                            "id": "2056370715",
                            "odds": "15.00",
                            "name": "26-30"
                        },
                        {
                            "id": "2056370716",
                            "odds": "13.00",
                            "name": "31+"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325854",
            "sp": {
                "winning_margin_12_way": {
                    "id": "180165",
                    "name": "Winning Margin 12-Way",
                    "odds": [
                        {
                            "id": "2056370717",
                            "odds": "5.50",
                            "header": "1",
                            "name": "1-5"
                        },
                        {
                            "id": "2056370718",
                            "odds": "6.50",
                            "header": "1",
                            "name": "6-10"
                        },
                        {
                            "id": "2056370719",
                            "odds": "9.00",
                            "header": "1",
                            "name": "11-15"
                        },
                        {
                            "id": "2056370720",
                            "odds": "15.00",
                            "header": "1",
                            "name": "16-20"
                        },
                        {
                            "id": "2056370721",
                            "odds": "21.00",
                            "header": "1",
                            "name": "21-25"
                        },
                        {
                            "id": "2056370722",
                            "odds": "11.00",
                            "header": "1",
                            "name": "26+"
                        },
                        {
                            "id": "2056370723",
                            "odds": "5.50",
                            "header": "2",
                            "name": "1-5"
                        },
                        {
                            "id": "2056370724",
                            "odds": "6.50",
                            "header": "2",
                            "name": "6-10"
                        },
                        {
                            "id": "2056370725",
                            "odds": "8.50",
                            "header": "2",
                            "name": "11-15"
                        },
                        {
                            "id": "2056370726",
                            "odds": "13.00",
                            "header": "2",
                            "name": "16-20"
                        },
                        {
                            "id": "2056370727",
                            "odds": "19.00",
                            "header": "2",
                            "name": "21-25"
                        },
                        {
                            "id": "2056370728",
                            "odds": "10.50",
                            "header": "2",
                            "name": "26+"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325714",
            "sp": {
                "2nd_quarter_total_odd_even": {
                    "id": "180171",
                    "name": "2nd Quarter Total - Odd\/Even",
                    "odds": [
                        {
                            "id": "2056370731",
                            "odds": "1.90",
                            "name": "Odd"
                        },
                        {
                            "id": "2056370732",
                            "odds": "1.90",
                            "name": "Even"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325960",
            "sp": {
                "alternative_point_spread_2": {
                    "id": "180968",
                    "name": "Alternative Point Spread 2",
                    "odds": [
                        {
                            "id": "2056372881",
                            "odds": "1.02",
                            "header": "1",
                            "handicap": "+25.5"
                        },
                        {
                            "id": "2056372875",
                            "odds": "1.05",
                            "header": "1",
                            "handicap": "+20.5"
                        },
                        {
                            "id": "2056372849",
                            "odds": "1.11",
                            "header": "1",
                            "handicap": "+15.5"
                        },
                        {
                            "id": "2056372825",
                            "odds": "1.25",
                            "header": "1",
                            "handicap": "+10.5"
                        },
                        {
                            "id": "2056372933",
                            "odds": "3.85",
                            "header": "1",
                            "handicap": "-9.5"
                        },
                        {
                            "id": "2056372959",
                            "odds": "5.75",
                            "header": "1",
                            "handicap": "-14.5"
                        },
                        {
                            "id": "2056372981",
                            "odds": "8.25",
                            "header": "1",
                            "handicap": "-19.5"
                        },
                        {
                            "id": "2056373005",
                            "odds": "10.50",
                            "header": "1",
                            "handicap": "-24.5"
                        },
                        {
                            "id": "2056372885",
                            "odds": "10.50",
                            "header": "2",
                            "handicap": "-25.5"
                        },
                        {
                            "id": "2056372876",
                            "odds": "8.25",
                            "header": "2",
                            "handicap": "-20.5"
                        },
                        {
                            "id": "2056372852",
                            "odds": "5.75",
                            "header": "2",
                            "handicap": "-15.5"
                        },
                        {
                            "id": "2056372828",
                            "odds": "3.75",
                            "header": "2",
                            "handicap": "-10.5"
                        },
                        {
                            "id": "2056372936",
                            "odds": "1.23",
                            "header": "2",
                            "handicap": "+9.5"
                        },
                        {
                            "id": "2056372960",
                            "odds": "1.11",
                            "header": "2",
                            "handicap": "+14.5"
                        },
                        {
                            "id": "2056372984",
                            "odds": "1.05",
                            "header": "2",
                            "handicap": "+19.5"
                        },
                        {
                            "id": "2056373008",
                            "odds": "1.02",
                            "header": "2",
                            "handicap": "+24.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325792",
            "sp": {
                "alternative_game_total_2": {
                    "id": "180979",
                    "name": "Alternative Game Total 2",
                    "odds": [
                        {
                            "id": "2056373230",
                            "odds": "1.07",
                            "header": "Over",
                            "name": "213.5"
                        },
                        {
                            "id": "2056373205",
                            "odds": "1.12",
                            "header": "Over",
                            "name": "218.5"
                        },
                        {
                            "id": "2056373178",
                            "odds": "1.21",
                            "header": "Over",
                            "name": "223.5"
                        },
                        {
                            "id": "2056373155",
                            "odds": "1.34",
                            "header": "Over",
                            "name": "228.5"
                        },
                        {
                            "id": "2056373232",
                            "odds": "7.50",
                            "header": "Under",
                            "name": "213.5"
                        },
                        {
                            "id": "2056373208",
                            "odds": "5.50",
                            "header": "Under",
                            "name": "218.5"
                        },
                        {
                            "id": "2056373180",
                            "odds": "4.25",
                            "header": "Under",
                            "name": "223.5"
                        },
                        {
                            "id": "2056373158",
                            "odds": "3.15",
                            "header": "Under",
                            "name": "228.5"
                        },
                        {
                            "id": "2056373054",
                            "odds": "2.85",
                            "header": "Over",
                            "name": "248.5"
                        },
                        {
                            "id": "2056373074",
                            "odds": "3.75",
                            "header": "Over",
                            "name": "253.5"
                        },
                        {
                            "id": "2056373099",
                            "odds": "4.75",
                            "header": "Over",
                            "name": "258.5"
                        },
                        {
                            "id": "2056373122",
                            "odds": "6.75",
                            "header": "Over",
                            "name": "263.5"
                        },
                        {
                            "id": "2056373055",
                            "odds": "1.38",
                            "header": "Under",
                            "name": "248.5"
                        },
                        {
                            "id": "2056373077",
                            "odds": "1.25",
                            "header": "Under",
                            "name": "253.5"
                        },
                        {
                            "id": "2056373101",
                            "odds": "1.15",
                            "header": "Under",
                            "name": "258.5"
                        },
                        {
                            "id": "2056373127",
                            "odds": "1.09",
                            "header": "Under",
                            "name": "263.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326034",
            "sp": {
                "game_total_(bands)_3_way": {
                    "id": "180999",
                    "name": "Game Total (Bands) 3-Way",
                    "odds": [
                        {
                            "id": "2056373451",
                            "odds": "1.86",
                            "name": "240 and Over"
                        },
                        {
                            "id": "2056373452",
                            "odds": "2.55",
                            "name": "220 - 239"
                        },
                        {
                            "id": "2056373453",
                            "odds": "5.50",
                            "name": "219 and Under"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325684",
            "sp": {
                "game_total_(bands)_8_way": {
                    "id": "181001",
                    "name": "Game Total (Bands) 8-Way",
                    "odds": [
                        {
                            "id": "2056373454",
                            "odds": "8.00",
                            "name": "0 - 214"
                        },
                        {
                            "id": "2056373455",
                            "odds": "15.00",
                            "name": "215 - 219"
                        },
                        {
                            "id": "2056373456",
                            "odds": "11.00",
                            "name": "220 - 224"
                        },
                        {
                            "id": "2056373457",
                            "odds": "9.50",
                            "name": "225 - 229"
                        },
                        {
                            "id": "2056373458",
                            "odds": "8.50",
                            "name": "230 - 234"
                        },
                        {
                            "id": "2056373459",
                            "odds": "8.00",
                            "name": "235 - 239"
                        },
                        {
                            "id": "2056373460",
                            "odds": "8.00",
                            "name": "240 - 244"
                        },
                        {
                            "id": "2056373461",
                            "odds": "2.35",
                            "name": "245+"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325605",
            "sp": {
                "alternative_team_totals": {
                    "id": "181005",
                    "name": "Alternative Team Totals",
                    "odds": [
                        {
                            "id": "2056373462",
                            "odds": "1.03",
                            "header": "Over",
                            "name": "98.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373464",
                            "odds": "1.05",
                            "header": "Over",
                            "name": "100.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373466",
                            "odds": "1.08",
                            "header": "Over",
                            "name": "102.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373468",
                            "odds": "1.11",
                            "header": "Over",
                            "name": "104.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373470",
                            "odds": "1.15",
                            "header": "Over",
                            "name": "106.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373488",
                            "odds": "1.21",
                            "header": "Over",
                            "name": "108.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373492",
                            "odds": "1.28",
                            "header": "Over",
                            "name": "110.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373494",
                            "odds": "1.36",
                            "header": "Over",
                            "name": "112.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373496",
                            "odds": "1.47",
                            "header": "Over",
                            "name": "114.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373498",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "116.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373500",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "122.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373502",
                            "odds": "2.60",
                            "header": "Over",
                            "name": "124.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373504",
                            "odds": "3.15",
                            "header": "Over",
                            "name": "126.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373506",
                            "odds": "3.65",
                            "header": "Over",
                            "name": "128.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373508",
                            "odds": "4.30",
                            "header": "Over",
                            "name": "130.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373257",
                            "odds": "4.75",
                            "header": "Over",
                            "name": "132.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373261",
                            "odds": "6.00",
                            "header": "Over",
                            "name": "134.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373263",
                            "odds": "7.00",
                            "header": "Over",
                            "name": "136.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373265",
                            "odds": "8.25",
                            "header": "Over",
                            "name": "138.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373267",
                            "odds": "9.50",
                            "header": "Over",
                            "name": "140.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373463",
                            "odds": "9.50",
                            "header": "Under",
                            "name": "98.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373465",
                            "odds": "8.25",
                            "header": "Under",
                            "name": "100.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373467",
                            "odds": "7.00",
                            "header": "Under",
                            "name": "102.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373469",
                            "odds": "6.00",
                            "header": "Under",
                            "name": "104.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373471",
                            "odds": "4.75",
                            "header": "Under",
                            "name": "106.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373491",
                            "odds": "4.25",
                            "header": "Under",
                            "name": "108.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373493",
                            "odds": "3.50",
                            "header": "Under",
                            "name": "110.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373495",
                            "odds": "3.00",
                            "header": "Under",
                            "name": "112.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373497",
                            "odds": "2.55",
                            "header": "Under",
                            "name": "114.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373499",
                            "odds": "2.20",
                            "header": "Under",
                            "name": "116.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373501",
                            "odds": "1.57",
                            "header": "Under",
                            "name": "122.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373503",
                            "odds": "1.45",
                            "header": "Under",
                            "name": "124.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373505",
                            "odds": "1.34",
                            "header": "Under",
                            "name": "126.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373507",
                            "odds": "1.26",
                            "header": "Under",
                            "name": "128.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373509",
                            "odds": "1.20",
                            "header": "Under",
                            "name": "130.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373260",
                            "odds": "1.15",
                            "header": "Under",
                            "name": "132.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373262",
                            "odds": "1.11",
                            "header": "Under",
                            "name": "134.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373264",
                            "odds": "1.08",
                            "header": "Under",
                            "name": "136.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373266",
                            "odds": "1.05",
                            "header": "Under",
                            "name": "138.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373268",
                            "odds": "1.03",
                            "header": "Under",
                            "name": "140.5",
                            "team": "1"
                        },
                        {
                            "id": "2056373269",
                            "odds": "1.04",
                            "header": "Over",
                            "name": "99.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373273",
                            "odds": "1.06",
                            "header": "Over",
                            "name": "101.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373277",
                            "odds": "1.08",
                            "header": "Over",
                            "name": "103.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373279",
                            "odds": "1.11",
                            "header": "Over",
                            "name": "105.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373286",
                            "odds": "1.16",
                            "header": "Over",
                            "name": "107.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373291",
                            "odds": "1.22",
                            "header": "Over",
                            "name": "109.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373293",
                            "odds": "1.30",
                            "header": "Over",
                            "name": "111.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373295",
                            "odds": "1.38",
                            "header": "Over",
                            "name": "113.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373297",
                            "odds": "1.50",
                            "header": "Over",
                            "name": "115.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373313",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "117.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373357",
                            "odds": "2.30",
                            "header": "Over",
                            "name": "123.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373396",
                            "odds": "2.70",
                            "header": "Over",
                            "name": "125.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373435",
                            "odds": "3.25",
                            "header": "Over",
                            "name": "127.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373437",
                            "odds": "3.75",
                            "header": "Over",
                            "name": "129.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373439",
                            "odds": "4.40",
                            "header": "Over",
                            "name": "131.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373441",
                            "odds": "5.00",
                            "header": "Over",
                            "name": "133.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373443",
                            "odds": "6.50",
                            "header": "Over",
                            "name": "135.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373445",
                            "odds": "7.50",
                            "header": "Over",
                            "name": "137.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373447",
                            "odds": "8.50",
                            "header": "Over",
                            "name": "139.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373449",
                            "odds": "9.50",
                            "header": "Over",
                            "name": "141.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373270",
                            "odds": "9.00",
                            "header": "Under",
                            "name": "99.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373274",
                            "odds": "8.00",
                            "header": "Under",
                            "name": "101.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373278",
                            "odds": "7.00",
                            "header": "Under",
                            "name": "103.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373280",
                            "odds": "5.75",
                            "header": "Under",
                            "name": "105.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373289",
                            "odds": "4.50",
                            "header": "Under",
                            "name": "107.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373292",
                            "odds": "4.00",
                            "header": "Under",
                            "name": "109.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373294",
                            "odds": "3.40",
                            "header": "Under",
                            "name": "111.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373296",
                            "odds": "2.85",
                            "header": "Under",
                            "name": "113.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373298",
                            "odds": "2.50",
                            "header": "Under",
                            "name": "115.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373318",
                            "odds": "2.20",
                            "header": "Under",
                            "name": "117.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373361",
                            "odds": "1.55",
                            "header": "Under",
                            "name": "123.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373400",
                            "odds": "1.41",
                            "header": "Under",
                            "name": "125.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373436",
                            "odds": "1.33",
                            "header": "Under",
                            "name": "127.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373438",
                            "odds": "1.25",
                            "header": "Under",
                            "name": "129.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373440",
                            "odds": "1.18",
                            "header": "Under",
                            "name": "131.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373442",
                            "odds": "1.14",
                            "header": "Under",
                            "name": "133.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373444",
                            "odds": "1.10",
                            "header": "Under",
                            "name": "135.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373446",
                            "odds": "1.07",
                            "header": "Under",
                            "name": "137.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373448",
                            "odds": "1.05",
                            "header": "Under",
                            "name": "139.5",
                            "team": "2"
                        },
                        {
                            "id": "2056373450",
                            "odds": "1.03",
                            "header": "Under",
                            "name": "141.5",
                            "team": "2"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325933",
            "sp": {
                "alternative_team_totals_2": {
                    "id": "181085",
                    "name": "Alternative Team Totals 2",
                    "odds": [
                        {
                            "id": "2056370765",
                            "odds": "1.01",
                            "header": "Over",
                            "name": "94.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370763",
                            "odds": "1.04",
                            "header": "Over",
                            "name": "99.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370759",
                            "odds": "1.23",
                            "header": "Over",
                            "name": "109.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370749",
                            "odds": "3.85",
                            "header": "Over",
                            "name": "129.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370753",
                            "odds": "8.75",
                            "header": "Over",
                            "name": "139.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370755",
                            "odds": "12.00",
                            "header": "Over",
                            "name": "144.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370766",
                            "odds": "12.00",
                            "header": "Under",
                            "name": "94.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370764",
                            "odds": "8.75",
                            "header": "Under",
                            "name": "99.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370760",
                            "odds": "3.85",
                            "header": "Under",
                            "name": "109.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370750",
                            "odds": "1.23",
                            "header": "Under",
                            "name": "129.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370754",
                            "odds": "1.04",
                            "header": "Under",
                            "name": "139.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370756",
                            "odds": "1.01",
                            "header": "Under",
                            "name": "144.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370785",
                            "odds": "1.01",
                            "header": "Over",
                            "name": "95.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370783",
                            "odds": "1.05",
                            "header": "Over",
                            "name": "100.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370779",
                            "odds": "1.25",
                            "header": "Over",
                            "name": "110.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370769",
                            "odds": "4.25",
                            "header": "Over",
                            "name": "130.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370773",
                            "odds": "9.00",
                            "header": "Over",
                            "name": "140.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370775",
                            "odds": "12.00",
                            "header": "Over",
                            "name": "145.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370786",
                            "odds": "11.50",
                            "header": "Under",
                            "name": "95.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370784",
                            "odds": "8.50",
                            "header": "Under",
                            "name": "100.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370780",
                            "odds": "3.75",
                            "header": "Under",
                            "name": "110.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370770",
                            "odds": "1.21",
                            "header": "Under",
                            "name": "130.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370774",
                            "odds": "1.04",
                            "header": "Under",
                            "name": "140.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370776",
                            "odds": "1.01",
                            "header": "Under",
                            "name": "145.5",
                            "team": "2"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325381",
            "sp": {
                "tied_at_end_of_regulation?": {
                    "id": "181127",
                    "name": "Tied at End Of Regulation?",
                    "odds": [
                        {
                            "id": "2056370795",
                            "odds": "13.25",
                            "name": "Yes"
                        },
                        {
                            "id": "2056370796",
                            "odds": "1.04",
                            "name": "No"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325544",
            "sp": {
                "highest_scoring_half": {
                    "id": "181131",
                    "name": "Highest Scoring Half",
                    "odds": [
                        {
                            "id": "2056370806",
                            "odds": "1.62",
                            "name": "1st Half"
                        },
                        {
                            "id": "2056370807",
                            "odds": "2.20",
                            "name": "2nd Half"
                        },
                        {
                            "id": "2056370808",
                            "odds": "26.00",
                            "name": "Tie"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326033",
            "sp": {
                "alternative_1st_half_point_spread": {
                    "id": "181137",
                    "name": "Alternative 1st Half Point Spread",
                    "odds": [
                        {
                            "id": "2056370802",
                            "odds": "5.25",
                            "header": "1",
                            "handicap": "-9.5"
                        },
                        {
                            "id": "2056370804",
                            "odds": "4.30",
                            "header": "1",
                            "handicap": "-7.5"
                        },
                        {
                            "id": "2056370809",
                            "odds": "3.40",
                            "header": "1",
                            "handicap": "-5.5"
                        },
                        {
                            "id": "2056370813",
                            "odds": "2.60",
                            "header": "1",
                            "handicap": "-3.5"
                        },
                        {
                            "id": "2056370815",
                            "odds": "2.10",
                            "header": "1",
                            "handicap": "-1.5"
                        },
                        {
                            "id": "2056370817",
                            "odds": "1.55",
                            "header": "1",
                            "handicap": "+2.5"
                        },
                        {
                            "id": "2056370819",
                            "odds": "1.38",
                            "header": "1",
                            "handicap": "+4.5"
                        },
                        {
                            "id": "2056370821",
                            "odds": "1.25",
                            "header": "1",
                            "handicap": "+6.5"
                        },
                        {
                            "id": "2056370823",
                            "odds": "1.16",
                            "header": "1",
                            "handicap": "+8.5"
                        },
                        {
                            "id": "2056370825",
                            "odds": "1.10",
                            "header": "1",
                            "handicap": "+10.5"
                        },
                        {
                            "id": "2056370803",
                            "odds": "1.13",
                            "header": "2",
                            "handicap": "+9.5"
                        },
                        {
                            "id": "2056370805",
                            "odds": "1.20",
                            "header": "2",
                            "handicap": "+7.5"
                        },
                        {
                            "id": "2056370810",
                            "odds": "1.30",
                            "header": "2",
                            "handicap": "+5.5"
                        },
                        {
                            "id": "2056370814",
                            "odds": "1.45",
                            "header": "2",
                            "handicap": "+3.5"
                        },
                        {
                            "id": "2056370816",
                            "odds": "1.66",
                            "header": "2",
                            "handicap": "+1.5"
                        },
                        {
                            "id": "2056370818",
                            "odds": "2.30",
                            "header": "2",
                            "handicap": "-2.5"
                        },
                        {
                            "id": "2056370820",
                            "odds": "2.85",
                            "header": "2",
                            "handicap": "-4.5"
                        },
                        {
                            "id": "2056370822",
                            "odds": "3.75",
                            "header": "2",
                            "handicap": "-6.5"
                        },
                        {
                            "id": "2056370824",
                            "odds": "4.50",
                            "header": "2",
                            "handicap": "-8.5"
                        },
                        {
                            "id": "2056370826",
                            "odds": "6.25",
                            "header": "2",
                            "handicap": "-10.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325954",
            "sp": {
                "alternative_1st_half_totals": {
                    "id": "181148",
                    "name": "Alternative 1st Half Totals",
                    "odds": [
                        {
                            "id": "2056370830",
                            "odds": "1.23",
                            "header": "Over",
                            "name": "112.5"
                        },
                        {
                            "id": "2056370832",
                            "odds": "1.31",
                            "header": "Over",
                            "name": "114.5"
                        },
                        {
                            "id": "2056370834",
                            "odds": "1.40",
                            "header": "Over",
                            "name": "116.5"
                        },
                        {
                            "id": "2056370836",
                            "odds": "1.52",
                            "header": "Over",
                            "name": "118.5"
                        },
                        {
                            "id": "2056370838",
                            "odds": "1.66",
                            "header": "Over",
                            "name": "120.5"
                        },
                        {
                            "id": "2056370831",
                            "odds": "3.85",
                            "header": "Under",
                            "name": "112.5"
                        },
                        {
                            "id": "2056370833",
                            "odds": "3.30",
                            "header": "Under",
                            "name": "114.5"
                        },
                        {
                            "id": "2056370835",
                            "odds": "2.75",
                            "header": "Under",
                            "name": "116.5"
                        },
                        {
                            "id": "2056370837",
                            "odds": "2.40",
                            "header": "Under",
                            "name": "118.5"
                        },
                        {
                            "id": "2056370839",
                            "odds": "2.10",
                            "header": "Under",
                            "name": "120.5"
                        },
                        {
                            "id": "2056370840",
                            "odds": "2.10",
                            "header": "Over",
                            "name": "124.5"
                        },
                        {
                            "id": "2056370842",
                            "odds": "2.40",
                            "header": "Over",
                            "name": "126.5"
                        },
                        {
                            "id": "2056370844",
                            "odds": "2.75",
                            "header": "Over",
                            "name": "128.5"
                        },
                        {
                            "id": "2056370846",
                            "odds": "3.30",
                            "header": "Over",
                            "name": "130.5"
                        },
                        {
                            "id": "2056370848",
                            "odds": "3.85",
                            "header": "Over",
                            "name": "132.5"
                        },
                        {
                            "id": "2056370841",
                            "odds": "1.66",
                            "header": "Under",
                            "name": "124.5"
                        },
                        {
                            "id": "2056370843",
                            "odds": "1.52",
                            "header": "Under",
                            "name": "126.5"
                        },
                        {
                            "id": "2056370845",
                            "odds": "1.40",
                            "header": "Under",
                            "name": "128.5"
                        },
                        {
                            "id": "2056370847",
                            "odds": "1.31",
                            "header": "Under",
                            "name": "130.5"
                        },
                        {
                            "id": "2056370849",
                            "odds": "1.23",
                            "header": "Under",
                            "name": "132.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325767",
            "sp": {
                "alternative_1st_half_team_totals": {
                    "id": "181160",
                    "name": "Alternative 1st Half Team Totals",
                    "odds": [
                        {
                            "id": "2056370857",
                            "odds": "1.12",
                            "header": "Over",
                            "name": "51.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370859",
                            "odds": "1.20",
                            "header": "Over",
                            "name": "53.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370861",
                            "odds": "1.30",
                            "header": "Over",
                            "name": "55.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370863",
                            "odds": "1.43",
                            "header": "Over",
                            "name": "57.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370865",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "59.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370867",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "63.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370869",
                            "odds": "2.85",
                            "header": "Over",
                            "name": "65.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370871",
                            "odds": "3.65",
                            "header": "Over",
                            "name": "67.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370873",
                            "odds": "4.50",
                            "header": "Over",
                            "name": "69.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370875",
                            "odds": "6.00",
                            "header": "Over",
                            "name": "71.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370858",
                            "odds": "5.50",
                            "header": "Under",
                            "name": "51.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370860",
                            "odds": "4.30",
                            "header": "Under",
                            "name": "53.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370862",
                            "odds": "3.40",
                            "header": "Under",
                            "name": "55.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370864",
                            "odds": "2.65",
                            "header": "Under",
                            "name": "57.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370866",
                            "odds": "2.20",
                            "header": "Under",
                            "name": "59.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370868",
                            "odds": "1.57",
                            "header": "Under",
                            "name": "63.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370870",
                            "odds": "1.38",
                            "header": "Under",
                            "name": "65.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370872",
                            "odds": "1.26",
                            "header": "Under",
                            "name": "67.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370874",
                            "odds": "1.16",
                            "header": "Under",
                            "name": "69.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370876",
                            "odds": "1.11",
                            "header": "Under",
                            "name": "71.5",
                            "team": "1"
                        },
                        {
                            "id": "2056370879",
                            "odds": "1.12",
                            "header": "Over",
                            "name": "51.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370881",
                            "odds": "1.20",
                            "header": "Over",
                            "name": "53.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370883",
                            "odds": "1.28",
                            "header": "Over",
                            "name": "55.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370885",
                            "odds": "1.43",
                            "header": "Over",
                            "name": "57.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370887",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "59.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370889",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "63.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370891",
                            "odds": "2.75",
                            "header": "Over",
                            "name": "65.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370893",
                            "odds": "3.65",
                            "header": "Over",
                            "name": "67.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370897",
                            "odds": "4.40",
                            "header": "Over",
                            "name": "69.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370899",
                            "odds": "6.00",
                            "header": "Over",
                            "name": "71.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370880",
                            "odds": "5.50",
                            "header": "Under",
                            "name": "51.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370882",
                            "odds": "4.30",
                            "header": "Under",
                            "name": "53.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370884",
                            "odds": "3.50",
                            "header": "Under",
                            "name": "55.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370886",
                            "odds": "2.65",
                            "header": "Under",
                            "name": "57.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370888",
                            "odds": "2.20",
                            "header": "Under",
                            "name": "59.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370890",
                            "odds": "1.57",
                            "header": "Under",
                            "name": "63.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370892",
                            "odds": "1.40",
                            "header": "Under",
                            "name": "65.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370894",
                            "odds": "1.26",
                            "header": "Under",
                            "name": "67.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370898",
                            "odds": "1.18",
                            "header": "Under",
                            "name": "69.5",
                            "team": "2"
                        },
                        {
                            "id": "2056370900",
                            "odds": "1.11",
                            "header": "Under",
                            "name": "71.5",
                            "team": "2"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326023",
            "sp": {
                "1st_half_double_chance": {
                    "id": "181184",
                    "name": "1st Half Double Chance",
                    "odds": [
                        {
                            "id": "2056370914",
                            "odds": "1.80",
                            "name": "OKC Thunder or Draw"
                        },
                        {
                            "id": "2056372787",
                            "odds": "1.80",
                            "name": "Draw or CHA Hornets"
                        },
                        {
                            "id": "2056372793",
                            "odds": "1.04",
                            "name": "OKC Thunder or CHA Hornets"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325472",
            "sp": {
                "1st_half_total_odd_even": {
                    "id": "181204",
                    "name": "1st Half Total Odd\/Even",
                    "odds": [
                        {
                            "id": "2056370980",
                            "odds": "1.90",
                            "name": "Odd"
                        },
                        {
                            "id": "2056370981",
                            "odds": "1.90",
                            "name": "Even"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325949",
            "sp": {
                "alternative_1st_quarter_point_spread": {
                    "id": "181206",
                    "name": "Alternative 1st Quarter Point Spread",
                    "odds": [
                        {
                            "id": "2056370994",
                            "odds": "3.65",
                            "header": "1",
                            "handicap": "-5.5"
                        },
                        {
                            "id": "2056370999",
                            "odds": "2.70",
                            "header": "1",
                            "handicap": "-3.5"
                        },
                        {
                            "id": "2056371007",
                            "odds": "2.20",
                            "header": "1",
                            "handicap": "-1.5"
                        },
                        {
                            "id": "2056371015",
                            "odds": "1.62",
                            "header": "1",
                            "handicap": "+1.5"
                        },
                        {
                            "id": "2056371022",
                            "odds": "1.31",
                            "header": "1",
                            "handicap": "+4.5"
                        },
                        {
                            "id": "2056371024",
                            "odds": "1.20",
                            "header": "1",
                            "handicap": "+6.5"
                        },
                        {
                            "id": "2056370997",
                            "odds": "1.26",
                            "header": "2",
                            "handicap": "+5.5"
                        },
                        {
                            "id": "2056371002",
                            "odds": "1.41",
                            "header": "2",
                            "handicap": "+3.5"
                        },
                        {
                            "id": "2056371010",
                            "odds": "1.62",
                            "header": "2",
                            "handicap": "+1.5"
                        },
                        {
                            "id": "2056371018",
                            "odds": "2.20",
                            "header": "2",
                            "handicap": "-1.5"
                        },
                        {
                            "id": "2056371023",
                            "odds": "3.30",
                            "header": "2",
                            "handicap": "-4.5"
                        },
                        {
                            "id": "2056371025",
                            "odds": "4.30",
                            "header": "2",
                            "handicap": "-6.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325842",
            "sp": {
                "alternative_1st_quarter_totals": {
                    "id": "181213",
                    "name": "Alternative 1st Quarter Totals",
                    "odds": [
                        {
                            "id": "2056371029",
                            "odds": "1.28",
                            "header": "Over",
                            "name": "55.5"
                        },
                        {
                            "id": "2056371033",
                            "odds": "1.41",
                            "header": "Over",
                            "name": "57.5"
                        },
                        {
                            "id": "2056371035",
                            "odds": "1.57",
                            "header": "Over",
                            "name": "59.5"
                        },
                        {
                            "id": "2056371030",
                            "odds": "3.50",
                            "header": "Under",
                            "name": "55.5"
                        },
                        {
                            "id": "2056371034",
                            "odds": "2.70",
                            "header": "Under",
                            "name": "57.5"
                        },
                        {
                            "id": "2056371036",
                            "odds": "2.25",
                            "header": "Under",
                            "name": "59.5"
                        },
                        {
                            "id": "2056371037",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "63.5"
                        },
                        {
                            "id": "2056371039",
                            "odds": "2.70",
                            "header": "Over",
                            "name": "65.5"
                        },
                        {
                            "id": "2056371041",
                            "odds": "3.50",
                            "header": "Over",
                            "name": "67.5"
                        },
                        {
                            "id": "2056371038",
                            "odds": "1.57",
                            "header": "Under",
                            "name": "63.5"
                        },
                        {
                            "id": "2056371040",
                            "odds": "1.41",
                            "header": "Under",
                            "name": "65.5"
                        },
                        {
                            "id": "2056371042",
                            "odds": "1.28",
                            "header": "Under",
                            "name": "67.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325558",
            "sp": {
                "alternative_1st_quarter_team_totals": {
                    "id": "181221",
                    "name": "Alternative 1st Quarter Team Totals",
                    "odds": [
                        {
                            "id": "2056371048",
                            "odds": "1.04",
                            "header": "Over",
                            "name": "21.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371050",
                            "odds": "1.10",
                            "header": "Over",
                            "name": "23.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371052",
                            "odds": "1.20",
                            "header": "Over",
                            "name": "25.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371054",
                            "odds": "1.34",
                            "header": "Over",
                            "name": "27.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371056",
                            "odds": "1.57",
                            "header": "Over",
                            "name": "29.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371071",
                            "odds": "2.65",
                            "header": "Over",
                            "name": "33.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371085",
                            "odds": "3.75",
                            "header": "Over",
                            "name": "35.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371107",
                            "odds": "5.25",
                            "header": "Over",
                            "name": "37.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371128",
                            "odds": "8.00",
                            "header": "Over",
                            "name": "39.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371141",
                            "odds": "10.50",
                            "header": "Over",
                            "name": "41.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371049",
                            "odds": "8.75",
                            "header": "Under",
                            "name": "21.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371051",
                            "odds": "6.50",
                            "header": "Under",
                            "name": "23.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371053",
                            "odds": "4.30",
                            "header": "Under",
                            "name": "25.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371055",
                            "odds": "3.15",
                            "header": "Under",
                            "name": "27.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371058",
                            "odds": "2.25",
                            "header": "Under",
                            "name": "29.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371079",
                            "odds": "1.43",
                            "header": "Under",
                            "name": "33.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371088",
                            "odds": "1.25",
                            "header": "Under",
                            "name": "35.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371109",
                            "odds": "1.13",
                            "header": "Under",
                            "name": "37.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371130",
                            "odds": "1.06",
                            "header": "Under",
                            "name": "39.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371146",
                            "odds": "1.02",
                            "header": "Under",
                            "name": "41.5",
                            "team": "1"
                        },
                        {
                            "id": "2056371181",
                            "odds": "1.03",
                            "header": "Over",
                            "name": "20.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371196",
                            "odds": "1.07",
                            "header": "Over",
                            "name": "22.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371217",
                            "odds": "1.15",
                            "header": "Over",
                            "name": "24.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371247",
                            "odds": "1.28",
                            "header": "Over",
                            "name": "26.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371262",
                            "odds": "1.50",
                            "header": "Over",
                            "name": "28.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371299",
                            "odds": "2.40",
                            "header": "Over",
                            "name": "32.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371312",
                            "odds": "3.40",
                            "header": "Over",
                            "name": "34.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371322",
                            "odds": "4.50",
                            "header": "Over",
                            "name": "36.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371334",
                            "odds": "7.00",
                            "header": "Over",
                            "name": "38.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371350",
                            "odds": "9.50",
                            "header": "Over",
                            "name": "40.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371187",
                            "odds": "9.50",
                            "header": "Under",
                            "name": "20.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371198",
                            "odds": "7.50",
                            "header": "Under",
                            "name": "22.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371221",
                            "odds": "4.75",
                            "header": "Under",
                            "name": "24.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371250",
                            "odds": "3.50",
                            "header": "Under",
                            "name": "26.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371264",
                            "odds": "2.50",
                            "header": "Under",
                            "name": "28.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371302",
                            "odds": "1.52",
                            "header": "Under",
                            "name": "32.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371314",
                            "odds": "1.30",
                            "header": "Under",
                            "name": "34.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371324",
                            "odds": "1.16",
                            "header": "Under",
                            "name": "36.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371338",
                            "odds": "1.08",
                            "header": "Under",
                            "name": "38.5",
                            "team": "2"
                        },
                        {
                            "id": "2056371351",
                            "odds": "1.03",
                            "header": "Under",
                            "name": "40.5",
                            "team": "2"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326011",
            "sp": {
                "1st_quarter_3_way_lines": {
                    "id": "181244",
                    "name": "1st Quarter 3 Way Lines",
                    "odds": [
                        {
                            "id": "2056371026",
                            "odds": "2.20",
                            "header": "1",
                            "name": "Spread",
                            "handicap": "-1.0"
                        },
                        {
                            "id": "2056371043",
                            "odds": "2.00",
                            "header": "1",
                            "name": "Total",
                            "handicap": "O 62.0"
                        },
                        {
                            "id": "2056371481",
                            "odds": "1.95",
                            "header": "1",
                            "name": "Money Line"
                        },
                        {
                            "id": "2056371027",
                            "odds": "13.00",
                            "header": "Tie",
                            "name": "Spread",
                            "handicap": "+1.0"
                        },
                        {
                            "id": "2056371044",
                            "odds": "17.00",
                            "header": "Tie",
                            "name": "Total",
                            "handicap": "E 62.0"
                        },
                        {
                            "id": "2056371485",
                            "odds": "13.00",
                            "header": "Tie",
                            "name": "Money Line"
                        },
                        {
                            "id": "2056371028",
                            "odds": "1.76",
                            "header": "2",
                            "name": "Spread",
                            "handicap": "+1.0"
                        },
                        {
                            "id": "2056371045",
                            "odds": "1.90",
                            "header": "2",
                            "name": "Total",
                            "handicap": "U 62.0"
                        },
                        {
                            "id": "2056371486",
                            "odds": "1.95",
                            "header": "2",
                            "name": "Money Line"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325640",
            "sp": {
                "1st_quarter_double_chance": {
                    "id": "181245",
                    "name": "1st Quarter Double Chance",
                    "odds": [
                        {
                            "id": "2056371487",
                            "odds": "1.71",
                            "name": "OKC Thunder or Draw"
                        },
                        {
                            "id": "2056372799",
                            "odds": "1.76",
                            "name": "Draw or CHA Hornets"
                        },
                        {
                            "id": "2056372804",
                            "odds": "1.04",
                            "name": "OKC Thunder or CHA Hornets"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325980",
            "sp": {
                "1st_quarter_team_to_score_x_points": {
                    "id": "181255",
                    "name": "1st Quarter Team To Score X Points",
                    "odds": [
                        {
                            "id": "2056371557",
                            "odds": "1.14",
                            "header": "Yes",
                            "name": "25",
                            "team": "1"
                        },
                        {
                            "id": "2056371565",
                            "odds": "1.62",
                            "header": "Yes",
                            "name": "30",
                            "team": "1"
                        },
                        {
                            "id": "2056371573",
                            "odds": "3.30",
                            "header": "Yes",
                            "name": "35",
                            "team": "1"
                        },
                        {
                            "id": "2056371562",
                            "odds": "5.00",
                            "header": "No",
                            "name": "25",
                            "team": "1"
                        },
                        {
                            "id": "2056371570",
                            "odds": "2.20",
                            "header": "No",
                            "name": "30",
                            "team": "1"
                        },
                        {
                            "id": "2056371576",
                            "odds": "1.31",
                            "header": "No",
                            "name": "35",
                            "team": "1"
                        },
                        {
                            "id": "2056371586",
                            "odds": "1.14",
                            "header": "Yes",
                            "name": "25",
                            "team": "2"
                        },
                        {
                            "id": "2056371631",
                            "odds": "1.62",
                            "header": "Yes",
                            "name": "30",
                            "team": "2"
                        },
                        {
                            "id": "2056371684",
                            "odds": "3.40",
                            "header": "Yes",
                            "name": "35",
                            "team": "2"
                        },
                        {
                            "id": "2056371591",
                            "odds": "5.00",
                            "header": "No",
                            "name": "25",
                            "team": "2"
                        },
                        {
                            "id": "2056371636",
                            "odds": "2.20",
                            "header": "No",
                            "name": "30",
                            "team": "2"
                        },
                        {
                            "id": "2056371689",
                            "odds": "1.30",
                            "header": "No",
                            "name": "35",
                            "team": "2"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325966",
            "sp": {
                "quarter_correct_score": {
                    "id": "181276",
                    "name": "Quarter Correct Score",
                    "odds": [
                        {
                            "id": "2056372416",
                            "odds": "11.00",
                            "header": "1",
                            "name": "2-1"
                        },
                        {
                            "id": "2056372420",
                            "odds": "26.00",
                            "header": "1",
                            "name": "3-0"
                        },
                        {
                            "id": "2056372422",
                            "odds": "4.20",
                            "header": "1",
                            "name": "3-1"
                        },
                        {
                            "id": "2056372424",
                            "odds": "15.00",
                            "header": "1",
                            "name": "4-0"
                        },
                        {
                            "id": "2056372426",
                            "odds": "11.00",
                            "header": "2",
                            "name": "2-1"
                        },
                        {
                            "id": "2056372427",
                            "odds": "26.00",
                            "header": "2",
                            "name": "3-0"
                        },
                        {
                            "id": "2056372429",
                            "odds": "4.20",
                            "header": "2",
                            "name": "3-1"
                        },
                        {
                            "id": "2056372431",
                            "odds": "15.00",
                            "header": "2",
                            "name": "4-0"
                        },
                        {
                            "id": "2056372433",
                            "odds": "2.90",
                            "name": "2-2"
                        },
                        {
                            "id": "2056372435",
                            "odds": "41.00",
                            "name": "Any Other"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325998",
            "sp": {
                "alternative_point_spread": {
                    "id": "181285",
                    "name": "Alternative Point Spread",
                    "odds": [
                        {
                            "id": "2056372568",
                            "odds": "3.15",
                            "header": "1",
                            "handicap": "-7.0"
                        },
                        {
                            "id": "2056372571",
                            "odds": "2.95",
                            "header": "1",
                            "handicap": "-6.5"
                        },
                        {
                            "id": "2056372573",
                            "odds": "2.85",
                            "header": "1",
                            "handicap": "-6.0"
                        },
                        {
                            "id": "2056372575",
                            "odds": "2.70",
                            "header": "1",
                            "handicap": "-5.5"
                        },
                        {
                            "id": "2056372577",
                            "odds": "2.65",
                            "header": "1",
                            "handicap": "-5.0"
                        },
                        {
                            "id": "2056372579",
                            "odds": "2.55",
                            "header": "1",
                            "handicap": "-4.5"
                        },
                        {
                            "id": "2056372581",
                            "odds": "2.50",
                            "header": "1",
                            "handicap": "-4.0"
                        },
                        {
                            "id": "2056372583",
                            "odds": "2.30",
                            "header": "1",
                            "handicap": "-3.5"
                        },
                        {
                            "id": "2056372585",
                            "odds": "2.25",
                            "header": "1",
                            "handicap": "-3.0"
                        },
                        {
                            "id": "2056372587",
                            "odds": "2.20",
                            "header": "1",
                            "handicap": "-2.5"
                        },
                        {
                            "id": "2056372588",
                            "odds": "2.10",
                            "header": "1",
                            "handicap": "-2.0"
                        },
                        {
                            "id": "2056372590",
                            "odds": "2.05",
                            "header": "1",
                            "handicap": "-1.5"
                        },
                        {
                            "id": "2056372592",
                            "odds": "1.95",
                            "header": "1",
                            "handicap": "-1.0"
                        },
                        {
                            "id": "2056372602",
                            "odds": "1.80",
                            "header": "1",
                            "handicap": "+1.5"
                        },
                        {
                            "id": "2056372604",
                            "odds": "1.76",
                            "header": "1",
                            "handicap": "+2.0"
                        },
                        {
                            "id": "2056372606",
                            "odds": "1.71",
                            "header": "1",
                            "handicap": "+2.5"
                        },
                        {
                            "id": "2056372607",
                            "odds": "1.66",
                            "header": "1",
                            "handicap": "+3.0"
                        },
                        {
                            "id": "2056372609",
                            "odds": "1.62",
                            "header": "1",
                            "handicap": "+3.5"
                        },
                        {
                            "id": "2056372611",
                            "odds": "1.57",
                            "header": "1",
                            "handicap": "+4.0"
                        },
                        {
                            "id": "2056372613",
                            "odds": "1.55",
                            "header": "1",
                            "handicap": "+4.5"
                        },
                        {
                            "id": "2056372615",
                            "odds": "1.50",
                            "header": "1",
                            "handicap": "+5.0"
                        },
                        {
                            "id": "2056372617",
                            "odds": "1.47",
                            "header": "1",
                            "handicap": "+5.5"
                        },
                        {
                            "id": "2056372618",
                            "odds": "1.43",
                            "header": "1",
                            "handicap": "+6.0"
                        },
                        {
                            "id": "2056372620",
                            "odds": "1.41",
                            "header": "1",
                            "handicap": "+6.5"
                        },
                        {
                            "id": "2056372622",
                            "odds": "1.38",
                            "header": "1",
                            "handicap": "+7.0"
                        },
                        {
                            "id": "2056372624",
                            "odds": "1.37",
                            "header": "1",
                            "handicap": "+7.5"
                        },
                        {
                            "id": "2056372626",
                            "odds": "1.34",
                            "header": "1",
                            "handicap": "+8.0"
                        },
                        {
                            "id": "2056372628",
                            "odds": "1.33",
                            "header": "1",
                            "handicap": "+8.5"
                        },
                        {
                            "id": "2056372630",
                            "odds": "1.30",
                            "header": "1",
                            "handicap": "+9.0"
                        },
                        {
                            "id": "2056372631",
                            "odds": "1.34",
                            "header": "2",
                            "handicap": "+7.0"
                        },
                        {
                            "id": "2056372633",
                            "odds": "1.37",
                            "header": "2",
                            "handicap": "+6.5"
                        },
                        {
                            "id": "2056372635",
                            "odds": "1.38",
                            "header": "2",
                            "handicap": "+6.0"
                        },
                        {
                            "id": "2056372637",
                            "odds": "1.41",
                            "header": "2",
                            "handicap": "+5.5"
                        },
                        {
                            "id": "2056372687",
                            "odds": "1.43",
                            "header": "2",
                            "handicap": "+5.0"
                        },
                        {
                            "id": "2056372689",
                            "odds": "1.47",
                            "header": "2",
                            "handicap": "+4.5"
                        },
                        {
                            "id": "2056372690",
                            "odds": "1.50",
                            "header": "2",
                            "handicap": "+4.0"
                        },
                        {
                            "id": "2056372693",
                            "odds": "1.55",
                            "header": "2",
                            "handicap": "+3.5"
                        },
                        {
                            "id": "2056372695",
                            "odds": "1.57",
                            "header": "2",
                            "handicap": "+3.0"
                        },
                        {
                            "id": "2056372697",
                            "odds": "1.62",
                            "header": "2",
                            "handicap": "+2.5"
                        },
                        {
                            "id": "2056372699",
                            "odds": "1.66",
                            "header": "2",
                            "handicap": "+2.0"
                        },
                        {
                            "id": "2056372701",
                            "odds": "1.68",
                            "header": "2",
                            "handicap": "+1.5"
                        },
                        {
                            "id": "2056372702",
                            "odds": "1.71",
                            "header": "2",
                            "handicap": "+1.0"
                        },
                        {
                            "id": "2056372736",
                            "odds": "1.90",
                            "header": "2",
                            "handicap": "-1.5"
                        },
                        {
                            "id": "2056372739",
                            "odds": "1.95",
                            "header": "2",
                            "handicap": "-2.0"
                        },
                        {
                            "id": "2056372740",
                            "odds": "2.00",
                            "header": "2",
                            "handicap": "-2.5"
                        },
                        {
                            "id": "2056372743",
                            "odds": "2.10",
                            "header": "2",
                            "handicap": "-3.0"
                        },
                        {
                            "id": "2056372745",
                            "odds": "2.20",
                            "header": "2",
                            "handicap": "-3.5"
                        },
                        {
                            "id": "2056372747",
                            "odds": "2.25",
                            "header": "2",
                            "handicap": "-4.0"
                        },
                        {
                            "id": "2056372748",
                            "odds": "2.30",
                            "header": "2",
                            "handicap": "-4.5"
                        },
                        {
                            "id": "2056372750",
                            "odds": "2.50",
                            "header": "2",
                            "handicap": "-5.0"
                        },
                        {
                            "id": "2056372752",
                            "odds": "2.55",
                            "header": "2",
                            "handicap": "-5.5"
                        },
                        {
                            "id": "2056372754",
                            "odds": "2.65",
                            "header": "2",
                            "handicap": "-6.0"
                        },
                        {
                            "id": "2056372756",
                            "odds": "2.70",
                            "header": "2",
                            "handicap": "-6.5"
                        },
                        {
                            "id": "2056372757",
                            "odds": "2.85",
                            "header": "2",
                            "handicap": "-7.0"
                        },
                        {
                            "id": "2056372759",
                            "odds": "2.95",
                            "header": "2",
                            "handicap": "-7.5"
                        },
                        {
                            "id": "2056372761",
                            "odds": "3.15",
                            "header": "2",
                            "handicap": "-8.0"
                        },
                        {
                            "id": "2056372763",
                            "odds": "3.25",
                            "header": "2",
                            "handicap": "-8.5"
                        },
                        {
                            "id": "2056372765",
                            "odds": "3.40",
                            "header": "2",
                            "handicap": "-9.0"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325745",
            "sp": {
                "alternative_game_total": {
                    "id": "181286",
                    "name": "Alternative Game Total",
                    "odds": [
                        {
                            "id": "2056372448",
                            "odds": "1.43",
                            "header": "Over",
                            "name": "231.0"
                        },
                        {
                            "id": "2056372453",
                            "odds": "1.45",
                            "header": "Over",
                            "name": "231.5"
                        },
                        {
                            "id": "2056372457",
                            "odds": "1.47",
                            "header": "Over",
                            "name": "232.0"
                        },
                        {
                            "id": "2056372461",
                            "odds": "1.50",
                            "header": "Over",
                            "name": "232.5"
                        },
                        {
                            "id": "2056372465",
                            "odds": "1.52",
                            "header": "Over",
                            "name": "233.0"
                        },
                        {
                            "id": "2056372469",
                            "odds": "1.54",
                            "header": "Over",
                            "name": "233.5"
                        },
                        {
                            "id": "2056372473",
                            "odds": "1.57",
                            "header": "Over",
                            "name": "234.0"
                        },
                        {
                            "id": "2056372477",
                            "odds": "1.58",
                            "header": "Over",
                            "name": "234.5"
                        },
                        {
                            "id": "2056372481",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "235.0"
                        },
                        {
                            "id": "2056372484",
                            "odds": "1.64",
                            "header": "Over",
                            "name": "235.5"
                        },
                        {
                            "id": "2056372488",
                            "odds": "1.66",
                            "header": "Over",
                            "name": "236.0"
                        },
                        {
                            "id": "2056372492",
                            "odds": "1.68",
                            "header": "Over",
                            "name": "236.5"
                        },
                        {
                            "id": "2056372495",
                            "odds": "1.71",
                            "header": "Over",
                            "name": "237.0"
                        },
                        {
                            "id": "2056372499",
                            "odds": "1.76",
                            "header": "Over",
                            "name": "237.5"
                        },
                        {
                            "id": "2056372503",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "238.0"
                        },
                        {
                            "id": "2056372506",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "238.5"
                        },
                        {
                            "id": "2056372451",
                            "odds": "2.65",
                            "header": "Under",
                            "name": "231.0"
                        },
                        {
                            "id": "2056372455",
                            "odds": "2.60",
                            "header": "Under",
                            "name": "231.5"
                        },
                        {
                            "id": "2056372459",
                            "odds": "2.55",
                            "header": "Under",
                            "name": "232.0"
                        },
                        {
                            "id": "2056372463",
                            "odds": "2.50",
                            "header": "Under",
                            "name": "232.5"
                        },
                        {
                            "id": "2056372467",
                            "odds": "2.40",
                            "header": "Under",
                            "name": "233.0"
                        },
                        {
                            "id": "2056372471",
                            "odds": "2.35",
                            "header": "Under",
                            "name": "233.5"
                        },
                        {
                            "id": "2056372475",
                            "odds": "2.25",
                            "header": "Under",
                            "name": "234.0"
                        },
                        {
                            "id": "2056372479",
                            "odds": "2.20",
                            "header": "Under",
                            "name": "234.5"
                        },
                        {
                            "id": "2056372482",
                            "odds": "2.15",
                            "header": "Under",
                            "name": "235.0"
                        },
                        {
                            "id": "2056372486",
                            "odds": "2.10",
                            "header": "Under",
                            "name": "235.5"
                        },
                        {
                            "id": "2056372490",
                            "odds": "2.05",
                            "header": "Under",
                            "name": "236.0"
                        },
                        {
                            "id": "2056372494",
                            "odds": "2.00",
                            "header": "Under",
                            "name": "236.5"
                        },
                        {
                            "id": "2056372497",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "237.0"
                        },
                        {
                            "id": "2056372501",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "237.5"
                        },
                        {
                            "id": "2056372504",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "238.0"
                        },
                        {
                            "id": "2056372508",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "238.5"
                        },
                        {
                            "id": "2056372513",
                            "odds": "1.95",
                            "header": "Over",
                            "name": "239.5"
                        },
                        {
                            "id": "2056372517",
                            "odds": "2.00",
                            "header": "Over",
                            "name": "240.0"
                        },
                        {
                            "id": "2056372520",
                            "odds": "2.05",
                            "header": "Over",
                            "name": "240.5"
                        },
                        {
                            "id": "2056372524",
                            "odds": "2.10",
                            "header": "Over",
                            "name": "241.0"
                        },
                        {
                            "id": "2056372527",
                            "odds": "2.15",
                            "header": "Over",
                            "name": "241.5"
                        },
                        {
                            "id": "2056372530",
                            "odds": "2.20",
                            "header": "Over",
                            "name": "242.0"
                        },
                        {
                            "id": "2056372533",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "242.5"
                        },
                        {
                            "id": "2056372537",
                            "odds": "2.30",
                            "header": "Over",
                            "name": "243.0"
                        },
                        {
                            "id": "2056372540",
                            "odds": "2.35",
                            "header": "Over",
                            "name": "243.5"
                        },
                        {
                            "id": "2056372544",
                            "odds": "2.40",
                            "header": "Over",
                            "name": "244.0"
                        },
                        {
                            "id": "2056372547",
                            "odds": "2.45",
                            "header": "Over",
                            "name": "244.5"
                        },
                        {
                            "id": "2056372551",
                            "odds": "2.50",
                            "header": "Over",
                            "name": "245.0"
                        },
                        {
                            "id": "2056372554",
                            "odds": "2.55",
                            "header": "Over",
                            "name": "245.5"
                        },
                        {
                            "id": "2056372557",
                            "odds": "2.60",
                            "header": "Over",
                            "name": "246.0"
                        },
                        {
                            "id": "2056372561",
                            "odds": "2.65",
                            "header": "Over",
                            "name": "246.5"
                        },
                        {
                            "id": "2056372565",
                            "odds": "2.70",
                            "header": "Over",
                            "name": "247.0"
                        },
                        {
                            "id": "2056372515",
                            "odds": "1.76",
                            "header": "Under",
                            "name": "239.5"
                        },
                        {
                            "id": "2056372518",
                            "odds": "1.74",
                            "header": "Under",
                            "name": "240.0"
                        },
                        {
                            "id": "2056372522",
                            "odds": "1.71",
                            "header": "Under",
                            "name": "240.5"
                        },
                        {
                            "id": "2056372525",
                            "odds": "1.68",
                            "header": "Under",
                            "name": "241.0"
                        },
                        {
                            "id": "2056372528",
                            "odds": "1.66",
                            "header": "Under",
                            "name": "241.5"
                        },
                        {
                            "id": "2056372532",
                            "odds": "1.64",
                            "header": "Under",
                            "name": "242.0"
                        },
                        {
                            "id": "2056372535",
                            "odds": "1.62",
                            "header": "Under",
                            "name": "242.5"
                        },
                        {
                            "id": "2056372538",
                            "odds": "1.60",
                            "header": "Under",
                            "name": "243.0"
                        },
                        {
                            "id": "2056372542",
                            "odds": "1.58",
                            "header": "Under",
                            "name": "243.5"
                        },
                        {
                            "id": "2056372545",
                            "odds": "1.57",
                            "header": "Under",
                            "name": "244.0"
                        },
                        {
                            "id": "2056372549",
                            "odds": "1.55",
                            "header": "Under",
                            "name": "244.5"
                        },
                        {
                            "id": "2056372552",
                            "odds": "1.52",
                            "header": "Under",
                            "name": "245.0"
                        },
                        {
                            "id": "2056372556",
                            "odds": "1.51",
                            "header": "Under",
                            "name": "245.5"
                        },
                        {
                            "id": "2056372559",
                            "odds": "1.50",
                            "header": "Under",
                            "name": "246.0"
                        },
                        {
                            "id": "2056372563",
                            "odds": "1.46",
                            "header": "Under",
                            "name": "246.5"
                        },
                        {
                            "id": "2056372566",
                            "odds": "1.45",
                            "header": "Under",
                            "name": "247.0"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326023",
            "sp": {
                "3rd_quarter_total_odd_even": {
                    "id": "181366",
                    "name": "3rd Quarter Total - Odd\/Even",
                    "odds": [
                        {
                            "id": "2056370737",
                            "odds": "1.90",
                            "name": "Odd"
                        },
                        {
                            "id": "2056370738",
                            "odds": "1.90",
                            "name": "Even"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326006",
            "sp": {
                "4th_quarter_total_odd_even": {
                    "id": "181368",
                    "name": "4th Quarter Total - Odd\/Even",
                    "odds": [
                        {
                            "id": "2056370742",
                            "odds": "1.90",
                            "name": "Odd"
                        },
                        {
                            "id": "2056370743",
                            "odds": "1.90",
                            "name": "Even"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325532",
            "sp": {
                "player_points": {
                    "id": "181378",
                    "name": "Player Points",
                    "odds": [
                        {
                            "id": "2051547751",
                            "odds": "1.80",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "Over",
                            "handicap": "13.5"
                        },
                        {
                            "id": "2051547979",
                            "odds": "1.86",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "Over",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051547633",
                            "odds": "1.90",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "Over",
                            "handicap": "31.5"
                        },
                        {
                            "id": "2051548078",
                            "odds": "1.95",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "Over",
                            "handicap": "12.5"
                        },
                        {
                            "id": "2051547887",
                            "odds": "1.86",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "Over",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051547461",
                            "odds": "1.86",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "Over",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051547514",
                            "odds": "1.95",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "Over",
                            "handicap": "11.5"
                        },
                        {
                            "id": "2051547520",
                            "odds": "1.83",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "Over",
                            "handicap": "21.5"
                        },
                        {
                            "id": "2051547916",
                            "odds": "1.86",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "Over",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051547752",
                            "odds": "1.95",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "Under",
                            "handicap": "13.5"
                        },
                        {
                            "id": "2051547980",
                            "odds": "1.86",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "Under",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051547634",
                            "odds": "1.83",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "Under",
                            "handicap": "31.5"
                        },
                        {
                            "id": "2051548080",
                            "odds": "1.80",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "Under",
                            "handicap": "12.5"
                        },
                        {
                            "id": "2051547888",
                            "odds": "1.86",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "Under",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051547463",
                            "odds": "1.86",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "Under",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051547515",
                            "odds": "1.80",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "Under",
                            "handicap": "11.5"
                        },
                        {
                            "id": "2051547521",
                            "odds": "1.90",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "Under",
                            "handicap": "21.5"
                        },
                        {
                            "id": "2051547917",
                            "odds": "1.86",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "Under",
                            "handicap": "15.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326039",
            "sp": {
                "player_assists": {
                    "id": "181379",
                    "name": "Player Assists",
                    "odds": [
                        {
                            "id": "2051549453",
                            "odds": "2.30",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051550628",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051548798",
                            "odds": "2.00",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051550751",
                            "odds": "2.40",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051549876",
                            "odds": "2.10",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "7.5"
                        },
                        {
                            "id": "2051548187",
                            "odds": "2.45",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051548299",
                            "odds": "1.74",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051548367",
                            "odds": "2.10",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051550049",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051549454",
                            "odds": "1.62",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051550630",
                            "odds": "1.64",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051548801",
                            "odds": "1.76",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051550752",
                            "odds": "1.58",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051549878",
                            "odds": "1.71",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "7.5"
                        },
                        {
                            "id": "2051548189",
                            "odds": "1.57",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051548300",
                            "odds": "2.05",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051548368",
                            "odds": "1.71",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051550057",
                            "odds": "2.30",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325359",
            "sp": {
                "player_rebounds": {
                    "id": "181380",
                    "name": "Player Rebounds",
                    "odds": [
                        {
                            "id": "2051550908",
                            "odds": "2.20",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051551162",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051550875",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "5.5"
                        },
                        {
                            "id": "2051551178",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051551009",
                            "odds": "1.71",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051550757",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "5.5"
                        },
                        {
                            "id": "2051550782",
                            "odds": "1.74",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "10.5"
                        },
                        {
                            "id": "2051550841",
                            "odds": "2.20",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051551072",
                            "odds": "1.90",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "5.5"
                        },
                        {
                            "id": "2051550909",
                            "odds": "1.66",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051551163",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051550876",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "5.5"
                        },
                        {
                            "id": "2051551179",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051551011",
                            "odds": "2.10",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051550758",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "5.5"
                        },
                        {
                            "id": "2051550784",
                            "odds": "2.05",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "10.5"
                        },
                        {
                            "id": "2051550842",
                            "odds": "1.66",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2051551073",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "5.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325980",
            "sp": {
                "player_steals": {
                    "id": "181381",
                    "name": "Player Steals",
                    "odds": [
                        {
                            "id": "2051551599",
                            "odds": "1.60",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551853",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551432",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051551867",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551740",
                            "odds": "1.90",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051551182",
                            "odds": "1.47",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551226",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551279",
                            "odds": "1.47",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551784",
                            "odds": "1.47",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551600",
                            "odds": "2.35",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551854",
                            "odds": "2.30",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551433",
                            "odds": "1.64",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051551869",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551742",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051551183",
                            "odds": "2.70",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551228",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551281",
                            "odds": "2.70",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051551786",
                            "odds": "2.70",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325978",
            "sp": {
                "player_turnovers": {
                    "id": "181382",
                    "name": "Player Turnovers",
                    "odds": [
                        {
                            "id": "2051552942",
                            "odds": "1.76",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051553427",
                            "odds": "1.57",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051552435",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051553443",
                            "odds": "1.74",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051553207",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051551877",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051551906",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051552008",
                            "odds": "2.45",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051553286",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051552944",
                            "odds": "2.00",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051553428",
                            "odds": "2.45",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051552436",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051553444",
                            "odds": "2.05",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051553209",
                            "odds": "1.64",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051551878",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051551908",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051552009",
                            "odds": "1.57",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051553287",
                            "odds": "1.64",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325797",
            "sp": {
                "player_blocks": {
                    "id": "181383",
                    "name": "Player Blocks",
                    "odds": [
                        {
                            "id": "2051553840",
                            "odds": "3.20",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554226",
                            "odds": "2.70",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553643",
                            "odds": "1.55",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554267",
                            "odds": "2.50",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553948",
                            "odds": "3.20",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553449",
                            "odds": "3.10",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553464",
                            "odds": "1.57",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553515",
                            "odds": "4.20",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554105",
                            "odds": "3.00",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051553842",
                            "odds": "1.35",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554227",
                            "odds": "1.47",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553645",
                            "odds": "2.50",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554268",
                            "odds": "1.55",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553949",
                            "odds": "1.35",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553450",
                            "odds": "1.38",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553465",
                            "odds": "2.45",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051553517",
                            "odds": "1.23",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554106",
                            "odds": "1.40",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325828",
            "sp": {
                "player_threes_made": {
                    "id": "181384",
                    "name": "Player Threes Made",
                    "odds": [
                        {
                            "id": "2051554409",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051554461",
                            "odds": "1.43",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554358",
                            "odds": "2.65",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051554570",
                            "odds": "1.64",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554417",
                            "odds": "1.71",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051554269",
                            "odds": "2.15",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051554295",
                            "odds": "2.15",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051554423",
                            "odds": "1.71",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051554410",
                            "odds": "2.30",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051554462",
                            "odds": "2.85",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554359",
                            "odds": "1.50",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051554571",
                            "odds": "2.25",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "0.5"
                        },
                        {
                            "id": "2051554418",
                            "odds": "2.10",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2051554270",
                            "odds": "1.68",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051554296",
                            "odds": "1.68",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051554424",
                            "odds": "2.10",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325927",
            "sp": {
                "player_points_and_assists": {
                    "id": "181387",
                    "name": "Player Points and Assists",
                    "odds": [
                        {
                            "id": "2051555325",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "16.5"
                        },
                        {
                            "id": "2051556571",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "21.5"
                        },
                        {
                            "id": "2051555079",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "37.5"
                        },
                        {
                            "id": "2051556674",
                            "odds": "1.90",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051555795",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "31.5"
                        },
                        {
                            "id": "2051554616",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "18.5"
                        },
                        {
                            "id": "2051554713",
                            "odds": "1.76",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "13.5"
                        },
                        {
                            "id": "2051554753",
                            "odds": "1.90",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "26.5"
                        },
                        {
                            "id": "2051556056",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "17.5"
                        },
                        {
                            "id": "2051555330",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "16.5"
                        },
                        {
                            "id": "2051556573",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "21.5"
                        },
                        {
                            "id": "2051555081",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "37.5"
                        },
                        {
                            "id": "2051556675",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051555798",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "31.5"
                        },
                        {
                            "id": "2051554617",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "18.5"
                        },
                        {
                            "id": "2051554714",
                            "odds": "2.00",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "13.5"
                        },
                        {
                            "id": "2051554754",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "26.5"
                        },
                        {
                            "id": "2051556060",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "17.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325968",
            "sp": {
                "player_points_and_rebounds": {
                    "id": "181388",
                    "name": "Player Points and Rebounds",
                    "odds": [
                        {
                            "id": "2051556825",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "18.5"
                        },
                        {
                            "id": "2051556865",
                            "odds": "1.90",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051556728",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "36.5"
                        },
                        {
                            "id": "2051556873",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "16.5"
                        },
                        {
                            "id": "2051556833",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "31.5"
                        },
                        {
                            "id": "2051556700",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "21.5"
                        },
                        {
                            "id": "2051556714",
                            "odds": "1.90",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "22.5"
                        },
                        {
                            "id": "2051556718",
                            "odds": "1.90",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "26.5"
                        },
                        {
                            "id": "2051556837",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "20.5"
                        },
                        {
                            "id": "2051556826",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "18.5"
                        },
                        {
                            "id": "2051556866",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051556729",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "36.5"
                        },
                        {
                            "id": "2051556874",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "16.5"
                        },
                        {
                            "id": "2051556834",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "31.5"
                        },
                        {
                            "id": "2051556701",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "21.5"
                        },
                        {
                            "id": "2051556715",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "22.5"
                        },
                        {
                            "id": "2051556719",
                            "odds": "1.83",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "26.5"
                        },
                        {
                            "id": "2051556838",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "20.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325748",
            "sp": {
                "player_assists_and_rebounds": {
                    "id": "181389",
                    "name": "Player Assists and Rebounds",
                    "odds": [
                        {
                            "id": "2051557056",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051557195",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "14.5"
                        },
                        {
                            "id": "2051556930",
                            "odds": "1.74",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "11.5"
                        },
                        {
                            "id": "2051557201",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "7.5"
                        },
                        {
                            "id": "2051557155",
                            "odds": "1.95",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "14.5"
                        },
                        {
                            "id": "2051556877",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051556881",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "13.5"
                        },
                        {
                            "id": "2051556895",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051557169",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "7.5"
                        },
                        {
                            "id": "2051557057",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "6.5"
                        },
                        {
                            "id": "2051557196",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "14.5"
                        },
                        {
                            "id": "2051556931",
                            "odds": "2.05",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "11.5"
                        },
                        {
                            "id": "2051557202",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "7.5"
                        },
                        {
                            "id": "2051557156",
                            "odds": "1.80",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "14.5"
                        },
                        {
                            "id": "2051556878",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051556882",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "13.5"
                        },
                        {
                            "id": "2051556896",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051557170",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "7.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325920",
            "sp": {
                "player_points,_assists_and_rebounds": {
                    "id": "181390",
                    "name": "Player Points, Assists and Rebounds",
                    "odds": [
                        {
                            "id": "2051558132",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "20.5"
                        },
                        {
                            "id": "2051559757",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "30.5"
                        },
                        {
                            "id": "2051557615",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "43.5"
                        },
                        {
                            "id": "2051560175",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "19.5"
                        },
                        {
                            "id": "2051558530",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "38.5"
                        },
                        {
                            "id": "2051557221",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051557269",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051557367",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "30.5"
                        },
                        {
                            "id": "2051558782",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "22.5"
                        },
                        {
                            "id": "2051558141",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "20.5"
                        },
                        {
                            "id": "2051559760",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "30.5"
                        },
                        {
                            "id": "2051557617",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "43.5"
                        },
                        {
                            "id": "2051560179",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "19.5"
                        },
                        {
                            "id": "2051558535",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "38.5"
                        },
                        {
                            "id": "2051557223",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051557271",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "24.5"
                        },
                        {
                            "id": "2051557368",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "30.5"
                        },
                        {
                            "id": "2051558786",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "22.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325750",
            "sp": {
                "player_steals_and_blocks": {
                    "id": "181391",
                    "name": "Player Steals and Blocks",
                    "odds": [
                        {
                            "id": "2051560932",
                            "odds": "2.70",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051561002",
                            "odds": "2.50",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560844",
                            "odds": "2.20",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051561041",
                            "odds": "2.75",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560978",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560356",
                            "odds": "2.25",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560452",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560599",
                            "odds": "2.60",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560980",
                            "odds": "2.60",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051560933",
                            "odds": "1.47",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051561003",
                            "odds": "1.55",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560846",
                            "odds": "1.66",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2051561042",
                            "odds": "1.45",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560979",
                            "odds": "2.30",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560359",
                            "odds": "1.64",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560454",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560602",
                            "odds": "1.52",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2051560981",
                            "odds": "1.52",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325422",
            "sp": {
                "player_points_low": {
                    "id": "181444",
                    "name": "Player Points Low",
                    "odds": [
                        {
                            "id": "2051561746",
                            "odds": "1.22",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051561922",
                            "odds": "1.22",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "11.5"
                        },
                        {
                            "id": "2051561507",
                            "odds": "1.27",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "25.5"
                        },
                        {
                            "id": "2051561958",
                            "odds": "1.28",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "7.5"
                        },
                        {
                            "id": "2051561865",
                            "odds": "1.25",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "19.5"
                        },
                        {
                            "id": "2051561091",
                            "odds": "1.27",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "10.5"
                        },
                        {
                            "id": "2051561277",
                            "odds": "1.28",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051561466",
                            "odds": "1.23",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "16.5"
                        },
                        {
                            "id": "2051561894",
                            "odds": "1.20",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "10.5"
                        },
                        {
                            "id": "2051561747",
                            "odds": "4.30",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051561923",
                            "odds": "4.30",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "11.5"
                        },
                        {
                            "id": "2051561508",
                            "odds": "3.70",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "25.5"
                        },
                        {
                            "id": "2051561960",
                            "odds": "3.65",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "7.5"
                        },
                        {
                            "id": "2051561867",
                            "odds": "4.10",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "19.5"
                        },
                        {
                            "id": "2051561093",
                            "odds": "3.80",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "10.5"
                        },
                        {
                            "id": "2051561280",
                            "odds": "3.65",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "8.5"
                        },
                        {
                            "id": "2051561468",
                            "odds": "4.20",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "16.5"
                        },
                        {
                            "id": "2051561895",
                            "odds": "4.60",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "10.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325448",
            "sp": {
                "player_points_high": {
                    "id": "181445",
                    "name": "Player Points High",
                    "odds": [
                        {
                            "id": "2051562567",
                            "odds": "4.90",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "20.5"
                        },
                        {
                            "id": "2051563331",
                            "odds": "5.50",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "20.5"
                        },
                        {
                            "id": "2051562311",
                            "odds": "4.90",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "38.5"
                        },
                        {
                            "id": "2051563355",
                            "odds": "5.25",
                            "header": "Over",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "18.5"
                        },
                        {
                            "id": "2051562788",
                            "odds": "5.25",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "30.5"
                        },
                        {
                            "id": "2051562031",
                            "odds": "4.90",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "23.5"
                        },
                        {
                            "id": "2051562091",
                            "odds": "4.90",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051562139",
                            "odds": "5.25",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "28.5"
                        },
                        {
                            "id": "2051562942",
                            "odds": "5.25",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "22.5"
                        },
                        {
                            "id": "2051562570",
                            "odds": "1.18",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "20.5"
                        },
                        {
                            "id": "2051563332",
                            "odds": "1.15",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "20.5"
                        },
                        {
                            "id": "2051562312",
                            "odds": "1.18",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "38.5"
                        },
                        {
                            "id": "2051563356",
                            "odds": "1.16",
                            "header": "Under",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "handicap": "18.5"
                        },
                        {
                            "id": "2051562790",
                            "odds": "1.16",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "30.5"
                        },
                        {
                            "id": "2051562032",
                            "odds": "1.18",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "23.5"
                        },
                        {
                            "id": "2051562092",
                            "odds": "1.18",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "15.5"
                        },
                        {
                            "id": "2051562141",
                            "odds": "1.16",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "28.5"
                        },
                        {
                            "id": "2051562944",
                            "odds": "1.16",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "22.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325889",
            "sp": {
                "player_points_milestones": {
                    "id": "181446",
                    "name": "Player Points Milestones",
                    "odds": [
                        {
                            "id": "2051563779",
                            "odds": "1.05",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051564270",
                            "odds": "1.11",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051563411",
                            "odds": "1.03",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051563470",
                            "odds": "1.01",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051563781",
                            "odds": "1.29",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051564152",
                            "odds": "1.09",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051564271",
                            "odds": "1.47",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051563413",
                            "odds": "1.20",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051563471",
                            "odds": "1.45",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051563480",
                            "odds": "1.02",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051564021",
                            "odds": "1.14",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051563783",
                            "odds": "1.95",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051564153",
                            "odds": "1.64",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051563621",
                            "odds": "1.01",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051564272",
                            "odds": "2.70",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051564013",
                            "odds": "1.04",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051563415",
                            "odds": "1.68",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051563472",
                            "odds": "3.80",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051563481",
                            "odds": "1.13",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051564022",
                            "odds": "1.71",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051563785",
                            "odds": "4.20",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "20"
                        },
                        {
                            "id": "2051564155",
                            "odds": "4.30",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "20"
                        },
                        {
                            "id": "2051563622",
                            "odds": "1.06",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "20"
                        },
                        {
                            "id": "2051564273",
                            "odds": "6.50",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "20"
                        },
                        {
                            "id": "2051564014",
                            "odds": "1.25",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "20"
                        },
                        {
                            "id": "2051563417",
                            "odds": "2.95",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "20"
                        },
                        {
                            "id": "2051563473",
                            "odds": "13.25",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "20"
                        },
                        {
                            "id": "2051563482",
                            "odds": "1.52",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "20"
                        },
                        {
                            "id": "2051564023",
                            "odds": "3.25",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "20"
                        },
                        {
                            "id": "2051563787",
                            "odds": "10.25",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "25"
                        },
                        {
                            "id": "2051564156",
                            "odds": "16.50",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "25"
                        },
                        {
                            "id": "2051563623",
                            "odds": "1.22",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "25"
                        },
                        {
                            "id": "2051564274",
                            "odds": "16.50",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "25"
                        },
                        {
                            "id": "2051564015",
                            "odds": "1.86",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "25"
                        },
                        {
                            "id": "2051563419",
                            "odds": "5.75",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "25"
                        },
                        {
                            "id": "2051563474",
                            "odds": "26.00",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "25"
                        },
                        {
                            "id": "2051563483",
                            "odds": "2.70",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "25"
                        },
                        {
                            "id": "2051564024",
                            "odds": "7.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "25"
                        },
                        {
                            "id": "2051563789",
                            "odds": "17.50",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "30"
                        },
                        {
                            "id": "2051564157",
                            "odds": "41.00",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "30"
                        },
                        {
                            "id": "2051563624",
                            "odds": "1.62",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "30"
                        },
                        {
                            "id": "2051564276",
                            "odds": "41.00",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "30"
                        },
                        {
                            "id": "2051564016",
                            "odds": "4.20",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "30"
                        },
                        {
                            "id": "2051563422",
                            "odds": "12.25",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "30"
                        },
                        {
                            "id": "2051563475",
                            "odds": "41.00",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "30"
                        },
                        {
                            "id": "2051563484",
                            "odds": "6.25",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "30"
                        },
                        {
                            "id": "2051564025",
                            "odds": "15.50",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "30"
                        },
                        {
                            "id": "2051563625",
                            "odds": "5.75",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "40"
                        },
                        {
                            "id": "2051564017",
                            "odds": "21.00",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "40"
                        },
                        {
                            "id": "2051563423",
                            "odds": "34.00",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "40"
                        },
                        {
                            "id": "2051563485",
                            "odds": "41.00",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "40"
                        },
                        {
                            "id": "2051564026",
                            "odds": "41.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "40"
                        },
                        {
                            "id": "2051563626",
                            "odds": "23.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "50"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325869",
            "sp": {
                "player_assists_milestones": {
                    "id": "181447",
                    "name": "Player Assists Milestones",
                    "odds": [
                        {
                            "id": "2051564741",
                            "odds": "2.30",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051564821",
                            "odds": "1.04",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051564588",
                            "odds": "1.03",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051564944",
                            "odds": "1.54",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051564770",
                            "odds": "1.04",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051564322",
                            "odds": "1.55",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051564370",
                            "odds": "1.74",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051564415",
                            "odds": "1.18",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051564778",
                            "odds": "3.05",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051564742",
                            "odds": "9.25",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051564822",
                            "odds": "1.30",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051564589",
                            "odds": "1.25",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051564945",
                            "odds": "4.20",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051564771",
                            "odds": "1.22",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051564324",
                            "odds": "4.30",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051564371",
                            "odds": "5.50",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051564417",
                            "odds": "2.10",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051564779",
                            "odds": "15.25",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051564743",
                            "odds": "23.00",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051564823",
                            "odds": "2.25",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051564591",
                            "odds": "2.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051564946",
                            "odds": "15.50",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051564772",
                            "odds": "1.68",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051564326",
                            "odds": "15.50",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051564372",
                            "odds": "17.00",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051564418",
                            "odds": "5.75",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051564780",
                            "odds": "41.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051564824",
                            "odds": "8.25",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051564592",
                            "odds": "7.25",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051564948",
                            "odds": "41.00",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051564773",
                            "odds": "3.40",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051564327",
                            "odds": "41.00",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051564420",
                            "odds": "19.00",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051564825",
                            "odds": "23.00",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "13"
                        },
                        {
                            "id": "2051564593",
                            "odds": "19.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "13"
                        },
                        {
                            "id": "2051564774",
                            "odds": "8.25",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "13"
                        },
                        {
                            "id": "2051564826",
                            "odds": "41.00",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051564594",
                            "odds": "41.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051564775",
                            "odds": "15.50",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "15"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325933",
            "sp": {
                "player_rebounds_milestones": {
                    "id": "181448",
                    "name": "Player Rebounds Milestones",
                    "odds": [
                        {
                            "id": "2051566666",
                            "odds": "1.20",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051567603",
                            "odds": "1.01",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051565765",
                            "odds": "1.06",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051567664",
                            "odds": "1.14",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051567220",
                            "odds": "1.01",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051565041",
                            "odds": "1.05",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051565212",
                            "odds": "1.20",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051567368",
                            "odds": "1.07",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051566671",
                            "odds": "2.20",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051567605",
                            "odds": "1.09",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051565768",
                            "odds": "1.42",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051567665",
                            "odds": "1.86",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051567225",
                            "odds": "1.16",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051565045",
                            "odds": "1.41",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051565113",
                            "odds": "1.01",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051565214",
                            "odds": "2.20",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051567370",
                            "odds": "1.47",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051566675",
                            "odds": "6.00",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051567607",
                            "odds": "1.33",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051565770",
                            "odds": "2.75",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051567666",
                            "odds": "4.60",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051567229",
                            "odds": "1.71",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051565047",
                            "odds": "2.70",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051565116",
                            "odds": "1.08",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051565217",
                            "odds": "6.00",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051567372",
                            "odds": "2.95",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051566683",
                            "odds": "21.00",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051567608",
                            "odds": "2.25",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051565774",
                            "odds": "12.25",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051567667",
                            "odds": "17.50",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "10"
                        },
                        {
                            "id": "2051567233",
                            "odds": "5.25",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051565049",
                            "odds": "11.75",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051565118",
                            "odds": "1.47",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051565220",
                            "odds": "19.00",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051567374",
                            "odds": "13.25",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "10"
                        },
                        {
                            "id": "2051567609",
                            "odds": "4.60",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "13"
                        },
                        {
                            "id": "2051565778",
                            "odds": "34.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "13"
                        },
                        {
                            "id": "2051567668",
                            "odds": "41.00",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "13"
                        },
                        {
                            "id": "2051567236",
                            "odds": "17.00",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "13"
                        },
                        {
                            "id": "2051565051",
                            "odds": "34.00",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "13"
                        },
                        {
                            "id": "2051565121",
                            "odds": "2.70",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "13"
                        },
                        {
                            "id": "2051567376",
                            "odds": "41.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "13"
                        },
                        {
                            "id": "2051567610",
                            "odds": "7.75",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051565782",
                            "odds": "41.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "15"
                        },
                        {
                            "id": "2051567241",
                            "odds": "34.00",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051565053",
                            "odds": "41.00",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051565126",
                            "odds": "4.30",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "15"
                        },
                        {
                            "id": "2051567611",
                            "odds": "13.25",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "17"
                        },
                        {
                            "id": "2051567246",
                            "odds": "41.00",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "17"
                        },
                        {
                            "id": "2051565130",
                            "odds": "7.25",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "17"
                        },
                        {
                            "id": "2051567612",
                            "odds": "19.00",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "20"
                        },
                        {
                            "id": "2051565132",
                            "odds": "16.00",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "header": "20"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326042",
            "sp": {
                "player_threes_made_milestones": {
                    "id": "181449",
                    "name": "Player Threes Made Milestones",
                    "odds": [
                        {
                            "id": "2051567821",
                            "odds": "1.13",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "1"
                        },
                        {
                            "id": "2051567923",
                            "odds": "1.43",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "1"
                        },
                        {
                            "id": "2051567712",
                            "odds": "1.34",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "1"
                        },
                        {
                            "id": "2051567945",
                            "odds": "1.64",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "1"
                        },
                        {
                            "id": "2051567844",
                            "odds": "1.01",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "1"
                        },
                        {
                            "id": "2051567672",
                            "odds": "1.25",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "1"
                        },
                        {
                            "id": "2051567682",
                            "odds": "1.07",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "1"
                        },
                        {
                            "id": "2051567862",
                            "odds": "1.15",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "1"
                        },
                        {
                            "id": "2051567822",
                            "odds": "1.62",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "2"
                        },
                        {
                            "id": "2051567924",
                            "odds": "3.15",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "2"
                        },
                        {
                            "id": "2051567713",
                            "odds": "2.65",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "2"
                        },
                        {
                            "id": "2051567946",
                            "odds": "4.30",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "2"
                        },
                        {
                            "id": "2051567845",
                            "odds": "1.07",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "2"
                        },
                        {
                            "id": "2051567673",
                            "odds": "2.15",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "2"
                        },
                        {
                            "id": "2051567683",
                            "odds": "1.37",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "2"
                        },
                        {
                            "id": "2051567863",
                            "odds": "1.71",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "2"
                        },
                        {
                            "id": "2051567823",
                            "odds": "3.05",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051567925",
                            "odds": "8.25",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051567714",
                            "odds": "6.50",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051567947",
                            "odds": "13.25",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "3"
                        },
                        {
                            "id": "2051567846",
                            "odds": "1.27",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051567674",
                            "odds": "4.90",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051567684",
                            "odds": "2.15",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051567864",
                            "odds": "3.25",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "3"
                        },
                        {
                            "id": "2051567824",
                            "odds": "6.25",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "4"
                        },
                        {
                            "id": "2051567926",
                            "odds": "17.00",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "4"
                        },
                        {
                            "id": "2051567715",
                            "odds": "16.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "4"
                        },
                        {
                            "id": "2051567948",
                            "odds": "21.00",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "4"
                        },
                        {
                            "id": "2051567847",
                            "odds": "1.71",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "4"
                        },
                        {
                            "id": "2051567675",
                            "odds": "12.25",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "4"
                        },
                        {
                            "id": "2051567685",
                            "odds": "4.10",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "4"
                        },
                        {
                            "id": "2051567865",
                            "odds": "7.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "4"
                        },
                        {
                            "id": "2051567825",
                            "odds": "15.25",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051567927",
                            "odds": "34.00",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051567716",
                            "odds": "26.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051567949",
                            "odds": "41.00",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder",
                            "header": "5"
                        },
                        {
                            "id": "2051567848",
                            "odds": "2.65",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051567676",
                            "odds": "19.00",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051567686",
                            "odds": "8.25",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051567866",
                            "odds": "16.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "5"
                        },
                        {
                            "id": "2051567826",
                            "odds": "19.00",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "6"
                        },
                        {
                            "id": "2051567928",
                            "odds": "41.00",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "header": "6"
                        },
                        {
                            "id": "2051567717",
                            "odds": "41.00",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "header": "6"
                        },
                        {
                            "id": "2051567849",
                            "odds": "4.30",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "6"
                        },
                        {
                            "id": "2051567677",
                            "odds": "41.00",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "header": "6"
                        },
                        {
                            "id": "2051567687",
                            "odds": "16.00",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "6"
                        },
                        {
                            "id": "2051567867",
                            "odds": "21.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "6"
                        },
                        {
                            "id": "2051567827",
                            "odds": "41.00",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "header": "7"
                        },
                        {
                            "id": "2051567850",
                            "odds": "7.75",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051567688",
                            "odds": "21.00",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051567868",
                            "odds": "41.00",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "header": "7"
                        },
                        {
                            "id": "2051567851",
                            "odds": "15.25",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "8"
                        },
                        {
                            "id": "2051567689",
                            "odds": "41.00",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "header": "8"
                        },
                        {
                            "id": "2051567852",
                            "odds": "18.00",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "9"
                        },
                        {
                            "id": "2051567853",
                            "odds": "29.00",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "header": "10"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325714",
            "sp": {
                "player_double_double": {
                    "id": "181463",
                    "name": "Player Double Double",
                    "odds": [
                        {
                            "id": "2051569109",
                            "odds": "2.15",
                            "header": "Yes",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051568418",
                            "odds": "5.50",
                            "header": "Yes",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051569265",
                            "odds": "17.50",
                            "header": "Yes",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051568786",
                            "odds": "2.65",
                            "header": "Yes",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051567961",
                            "odds": "15.50",
                            "header": "Yes",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051568053",
                            "odds": "2.00",
                            "header": "Yes",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051568180",
                            "odds": "17.50",
                            "header": "Yes",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051568896",
                            "odds": "16.00",
                            "header": "Yes",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051569110",
                            "odds": "1.68",
                            "header": "No",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051568419",
                            "odds": "1.15",
                            "header": "No",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051569268",
                            "odds": "1.01",
                            "header": "No",
                            "name": "Jalen Williams",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051568789",
                            "odds": "1.50",
                            "header": "No",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051567964",
                            "odds": "1.02",
                            "header": "No",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051568056",
                            "odds": "1.76",
                            "header": "No",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051568182",
                            "odds": "1.01",
                            "header": "No",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051568898",
                            "odds": "1.02",
                            "header": "No",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672326021",
            "sp": {
                "player_triple_double": {
                    "id": "181464",
                    "name": "Player Triple Double",
                    "odds": [
                        {
                            "id": "2051572142",
                            "odds": "12.25",
                            "header": "Yes",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051571230",
                            "odds": "12.25",
                            "header": "Yes",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets"
                        },
                        {
                            "id": "2051572144",
                            "odds": "1.04",
                            "header": "No",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder"
                        },
                        {
                            "id": "2051571233",
                            "odds": "1.04",
                            "header": "No",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325978",
            "sp": {
                "1st_quarter_player_points": {
                    "id": "181477",
                    "name": "1st Quarter Player Points",
                    "odds": [
                        {
                            "id": "2053983736",
                            "odds": "1.68",
                            "header": "Over",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2053984116",
                            "odds": "1.76",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2053983544",
                            "odds": "1.76",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "9.5"
                        },
                        {
                            "id": "2053983854",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "5.5"
                        },
                        {
                            "id": "2053982734",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2053983075",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2053984026",
                            "odds": "1.66",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2053983739",
                            "odds": "2.15",
                            "header": "Under",
                            "name": "Luguentz Dort",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2053984118",
                            "odds": "2.00",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "3.5"
                        },
                        {
                            "id": "2053983549",
                            "odds": "2.00",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "9.5"
                        },
                        {
                            "id": "2053983856",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "5.5"
                        },
                        {
                            "id": "2053982737",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2053983086",
                            "odds": "2.30",
                            "header": "Under",
                            "name": "Terry Rozier",
                            "name2": "CHA Hornets",
                            "handicap": "4.5"
                        },
                        {
                            "id": "2053984028",
                            "odds": "2.20",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "3.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325987",
            "sp": {
                "1st_quarter_player_assists": {
                    "id": "181478",
                    "name": "1st Quarter Player Assists",
                    "odds": [
                        {
                            "id": "2053984407",
                            "odds": "1.83",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984171",
                            "odds": "1.62",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984362",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984408",
                            "odds": "1.90",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984173",
                            "odds": "2.30",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984364",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        }
                    ]
                }
            }
        },
        {
            "updated_at": "1672325979",
            "sp": {
                "1st_quarter_player_rebounds": {
                    "id": "181479",
                    "name": "1st Quarter Player Rebounds",
                    "odds": [
                        {
                            "id": "2053984834",
                            "odds": "2.65",
                            "header": "Over",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2053984492",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984604",
                            "odds": "1.86",
                            "header": "Over",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984415",
                            "odds": "1.95",
                            "header": "Over",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984419",
                            "odds": "1.80",
                            "header": "Over",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2053984614",
                            "odds": "2.20",
                            "header": "Over",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984835",
                            "odds": "1.50",
                            "header": "Under",
                            "name": "Josh Giddey",
                            "name2": "OKC Thunder",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2053984495",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "Shai Gilgeous-Alexander",
                            "name2": "OKC Thunder",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984605",
                            "odds": "1.86",
                            "header": "Under",
                            "name": "LaMelo Ball",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984416",
                            "odds": "1.80",
                            "header": "Under",
                            "name": "Gordon Hayward",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        },
                        {
                            "id": "2053984420",
                            "odds": "1.95",
                            "header": "Under",
                            "name": "Mason Plumlee",
                            "name2": "CHA Hornets",
                            "handicap": "2.5"
                        },
                        {
                            "id": "2053984615",
                            "odds": "1.66",
                            "header": "Under",
                            "name": "PJ Washington",
                            "name2": "CHA Hornets",
                            "handicap": "1.5"
                        }
                    ]
                }
            }
        }
    ],
    "player_props": {
        "updated_at": "1672325953",
        "key": "#AC#B18#C20604387#D19#E15942762#F19#I43#",
        "sp": {
            "player_points": {
                "id": "181378",
                "name": "Player Points",
                "odds": [
                    {
                        "id": "2051547751",
                        "odds": "1.80",
                        "name": "Luguentz Dort",
                        "name2": "OKC Thunder",
                        "header": "Over",
                        "handicap": "13.5"
                    },
                    {
                        "id": "2051547979",
                        "odds": "1.86",
                        "name": "Josh Giddey",
                        "name2": "OKC Thunder",
                        "header": "Over",
                        "handicap": "15.5"
                    },
                    {
                        "id": "2051547633",
                        "odds": "1.90",
                        "name": "Shai Gilgeous-Alexander",
                        "name2": "OKC Thunder",
                        "header": "Over",
                        "handicap": "31.5"
                    },
                    {
                        "id": "2051548078",
                        "odds": "1.95",
                        "name": "Jalen Williams",
                        "name2": "OKC Thunder",
                        "header": "Over",
                        "handicap": "12.5"
                    },
                    {
                        "id": "2051547887",
                        "odds": "1.86",
                        "name": "LaMelo Ball",
                        "name2": "CHA Hornets",
                        "header": "Over",
                        "handicap": "24.5"
                    },
                    {
                        "id": "2051547461",
                        "odds": "1.86",
                        "name": "Gordon Hayward",
                        "name2": "CHA Hornets",
                        "header": "Over",
                        "handicap": "15.5"
                    },
                    {
                        "id": "2051547752",
                        "odds": "1.95",
                        "name": "Luguentz Dort",
                        "name2": "OKC Thunder",
                        "header": "Under",
                        "handicap": "13.5"
                    },
                    {
                        "id": "2051547980",
                        "odds": "1.86",
                        "name": "Josh Giddey",
                        "name2": "OKC Thunder",
                        "header": "Under",
                        "handicap": "15.5"
                    },
                    {
                        "id": "2051547634",
                        "odds": "1.83",
                        "name": "Shai Gilgeous-Alexander",
                        "name2": "OKC Thunder",
                        "header": "Under",
                        "handicap": "31.5"
                    },
                    {
                        "id": "2051548080",
                        "odds": "1.80",
                        "name": "Jalen Williams",
                        "name2": "OKC Thunder",
                        "header": "Under",
                        "handicap": "12.5"
                    },
                    {
                        "id": "2051547888",
                        "odds": "1.86",
                        "name": "LaMelo Ball",
                        "name2": "CHA Hornets",
                        "header": "Under",
                        "handicap": "24.5"
                    },
                    {
                        "id": "2051547463",
                        "odds": "1.86",
                        "name": "Gordon Hayward",
                        "name2": "CHA Hornets",
                        "header": "Under",
                        "handicap": "15.5"
                    }
                ]
            },
            "player_points_low": {
                "id": "181444",
                "name": "Player Points Low",
                "odds": []
            },
            "player_points_high": {
                "id": "181445",
                "name": "Player Points High",
                "odds": []
            },
            "player_points_milestones": {
                "id": "181446",
                "name": "Player Points Milestones",
                "odds": []
            },
            "1st_quarter_player_points": {
                "id": "181477",
                "name": "1st Quarter Player Points",
                "odds": []
            },
            "player_assists": {
                "id": "181379",
                "name": "Player Assists",
                "odds": []
            },
            "player_assists_milestones": {
                "id": "181447",
                "name": "Player Assists Milestones",
                "odds": []
            },
            "1st_quarter_player_assists": {
                "id": "181478",
                "name": "1st Quarter Player Assists",
                "odds": []
            },
            "player_rebounds": {
                "id": "181380",
                "name": "Player Rebounds",
                "odds": []
            },
            "player_rebounds_milestones": {
                "id": "181448",
                "name": "Player Rebounds Milestones",
                "odds": []
            },
            "1st_quarter_player_rebounds": {
                "id": "181479",
                "name": "1st Quarter Player Rebounds",
                "odds": []
            },
            "player_steals": {
                "id": "181381",
                "name": "Player Steals",
                "odds": []
            },
            "player_turnovers": {
                "id": "181382",
                "name": "Player Turnovers",
                "odds": []
            },
            "player_blocks": {
                "id": "181383",
                "name": "Player Blocks",
                "odds": []
            },
            "player_threes_made": {
                "id": "181384",
                "name": "Player Threes Made",
                "odds": []
            },
            "player_threes_made_milestones": {
                "id": "181449",
                "name": "Player Threes Made Milestones",
                "odds": []
            },
            "player_double_double": {
                "id": "181463",
                "name": "Player Double Double",
                "odds": []
            },
            "player_triple_double": {
                "id": "181464",
                "name": "Player Triple Double",
                "odds": []
            },
            "player_points_and_assists": {
                "id": "181387",
                "name": "Player Points and Assists",
                "odds": []
            },
            "player_points_and_rebounds": {
                "id": "181388",
                "name": "Player Points and Rebounds",
                "odds": []
            },
            "player_assists_and_rebounds": {
                "id": "181389",
                "name": "Player Assists and Rebounds",
                "odds": []
            },
            "player_points,_assists_and_rebounds": {
                "id": "181390",
                "name": "Player Points, Assists and Rebounds",
                "odds": []
            },
            "player_steals_and_blocks": {
                "id": "181391",
                "name": "Player Steals and Blocks",
                "odds": []
            }
        }
    },
    "quarter_props": {
        "updated_at": "1672325835",
        "key": "#AC#B18#C20604387#D19#E15942762#F19#I3#",
        "sp": {
            "alternative_1st_quarter_point_spread": {
                "id": "181206",
                "name": "Alternative 1st Quarter Point Spread",
                "odds": []
            },
            "alternative_1st_quarter_totals": {
                "id": "181213",
                "name": "Alternative 1st Quarter Totals",
                "odds": []
            },
            "alternative_1st_quarter_team_totals": {
                "id": "181221",
                "name": "Alternative 1st Quarter Team Totals",
                "odds": [
                    {
                        "id": "2056371048",
                        "odds": "1.05",
                        "header": "Over",
                        "name": "21.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371050",
                        "odds": "1.10",
                        "header": "Over",
                        "name": "23.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371052",
                        "odds": "1.20",
                        "header": "Over",
                        "name": "25.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371054",
                        "odds": "1.35",
                        "header": "Over",
                        "name": "27.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371056",
                        "odds": "1.62",
                        "header": "Over",
                        "name": "29.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371071",
                        "odds": "2.70",
                        "header": "Over",
                        "name": "33.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371049",
                        "odds": "8.50",
                        "header": "Under",
                        "name": "21.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371051",
                        "odds": "6.50",
                        "header": "Under",
                        "name": "23.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371053",
                        "odds": "4.30",
                        "header": "Under",
                        "name": "25.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371055",
                        "odds": "3.05",
                        "header": "Under",
                        "name": "27.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371058",
                        "odds": "2.20",
                        "header": "Under",
                        "name": "29.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371079",
                        "odds": "1.41",
                        "header": "Under",
                        "name": "33.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371181",
                        "odds": "1.03",
                        "header": "Over",
                        "name": "20.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371196",
                        "odds": "1.07",
                        "header": "Over",
                        "name": "22.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371217",
                        "odds": "1.14",
                        "header": "Over",
                        "name": "24.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371247",
                        "odds": "1.26",
                        "header": "Over",
                        "name": "26.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371262",
                        "odds": "1.47",
                        "header": "Over",
                        "name": "28.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371299",
                        "odds": "2.40",
                        "header": "Over",
                        "name": "32.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371187",
                        "odds": "10.00",
                        "header": "Under",
                        "name": "20.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371198",
                        "odds": "7.50",
                        "header": "Under",
                        "name": "22.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371221",
                        "odds": "5.00",
                        "header": "Under",
                        "name": "24.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371250",
                        "odds": "3.65",
                        "header": "Under",
                        "name": "26.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371264",
                        "odds": "2.55",
                        "header": "Under",
                        "name": "28.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371302",
                        "odds": "1.52",
                        "header": "Under",
                        "name": "32.5",
                        "team": "2"
                    }
                ]
            },
            "1st_quarter_both_teams_to_score_x_points": {
                "id": "181252",
                "name": "1st Quarter Both Teams to Score X Points",
                "odds": [
                    {
                        "id": "2056371522",
                        "odds": "1.15",
                        "header": "Yes",
                        "name": "22"
                    },
                    {
                        "id": "2056371542",
                        "odds": "1.43",
                        "header": "Yes",
                        "name": "25"
                    },
                    {
                        "id": "2056371549",
                        "odds": "3.25",
                        "header": "Yes",
                        "name": "30"
                    },
                    {
                        "id": "2056371523",
                        "odds": "4.75",
                        "header": "No",
                        "name": "22"
                    },
                    {
                        "id": "2056371546",
                        "odds": "2.65",
                        "header": "No",
                        "name": "25"
                    },
                    {
                        "id": "2056371554",
                        "odds": "1.33",
                        "header": "No",
                        "name": "30"
                    }
                ]
            },
            "1st_quarter_double_chance": {
                "id": "181245",
                "name": "1st Quarter Double Chance",
                "odds": []
            },
            "1st_quarter_handicap_and_total": {
                "id": "181243",
                "name": "1st Quarter Handicap and Total",
                "odds": [
                    {
                        "id": "2057512965",
                        "odds": "3.75",
                        "name": "OKC Thunder -0.5 & Over 61.5"
                    },
                    {
                        "id": "2057512967",
                        "odds": "3.40",
                        "name": "CHA Hornets +0.5 & Over 61.5"
                    },
                    {
                        "id": "2057512966",
                        "odds": "3.75",
                        "name": "OKC Thunder -0.5 & Under 61.5"
                    },
                    {
                        "id": "2057512968",
                        "odds": "3.50",
                        "name": "CHA Hornets +0.5 & Under 61.5"
                    }
                ]
            },
            "1st_quarter_margin_of_victory": {
                "id": "180180",
                "name": "1st Quarter Margin Of Victory",
                "odds": [
                    {
                        "id": "2056372767",
                        "odds": "2.40",
                        "header": "1",
                        "name": "3 or more"
                    },
                    {
                        "id": "2056372770",
                        "odds": "2.45",
                        "header": "2",
                        "name": "3 or more"
                    },
                    {
                        "id": "2056372772",
                        "odds": "3.60",
                        "name": "Any Other Result"
                    }
                ]
            },
            "1st_quarter_3_way_lines": {
                "id": "181244",
                "name": "1st Quarter 3 Way Lines",
                "odds": []
            },
            "1st_quarter_race_to_(points)": {
                "id": "181248",
                "name": "1st Quarter Race To (Points)",
                "odds": [
                    {
                        "id": "2056371512",
                        "odds": "1.83",
                        "header": "1",
                        "name": "10"
                    },
                    {
                        "id": "2056371515",
                        "odds": "1.83",
                        "header": "1",
                        "name": "15"
                    },
                    {
                        "id": "2056371518",
                        "odds": "1.83",
                        "header": "1",
                        "name": "20"
                    },
                    {
                        "id": "2056371513",
                        "odds": "1.83",
                        "header": "2",
                        "name": "10"
                    },
                    {
                        "id": "2056371516",
                        "odds": "1.83",
                        "header": "2",
                        "name": "15"
                    },
                    {
                        "id": "2056371519",
                        "odds": "1.83",
                        "header": "2",
                        "name": "20"
                    },
                    {
                        "id": "2056371514",
                        "odds": "101.00",
                        "header": "Neither",
                        "name": "10"
                    },
                    {
                        "id": "2056371517",
                        "odds": "101.00",
                        "header": "Neither",
                        "name": "15"
                    },
                    {
                        "id": "2056371521",
                        "odds": "81.00",
                        "header": "Neither",
                        "name": "20"
                    }
                ]
            },
            "1st_quarter_result_and_total": {
                "id": "181242",
                "name": "1st Quarter Result and Total",
                "odds": [
                    {
                        "id": "2056371353",
                        "odds": "3.75",
                        "header": "Over",
                        "name": "1",
                        "handicap": "61.5"
                    },
                    {
                        "id": "2056371368",
                        "odds": "3.80",
                        "header": "Over",
                        "name": "2",
                        "handicap": "61.5"
                    },
                    {
                        "id": "2056371419",
                        "odds": "23.00",
                        "header": "Over",
                        "name": "Tie",
                        "handicap": "61.5"
                    },
                    {
                        "id": "2056371367",
                        "odds": "3.75",
                        "header": "Under",
                        "name": "1",
                        "handicap": "61.5"
                    },
                    {
                        "id": "2056371407",
                        "odds": "3.80",
                        "header": "Under",
                        "name": "2",
                        "handicap": "61.5"
                    },
                    {
                        "id": "2056371421",
                        "odds": "23.00",
                        "header": "Under",
                        "name": "Tie",
                        "handicap": "61.5"
                    }
                ]
            },
            "1st_quarter_team_totals": {
                "id": "181220",
                "name": "1st Quarter Team Totals",
                "odds": [
                    {
                        "id": "2056371046",
                        "odds": "2.00",
                        "header": "1",
                        "handicap": "Over 31.5"
                    },
                    {
                        "id": "2056371047",
                        "odds": "1.71",
                        "header": "1",
                        "handicap": "Under 31.5"
                    },
                    {
                        "id": "2056371154",
                        "odds": "1.80",
                        "header": "2",
                        "handicap": "Over 30.5"
                    },
                    {
                        "id": "2056371157",
                        "odds": "1.86",
                        "header": "2",
                        "handicap": "Under 30.5"
                    }
                ]
            },
            "1st_quarter_team_to_score_x_points": {
                "id": "181255",
                "name": "1st Quarter Team To Score X Points",
                "odds": []
            },
            "1st_quarter_total_odd_even": {
                "id": "180170",
                "name": "1st Quarter Total - Odd\/Even",
                "odds": [
                    {
                        "id": "2056370729",
                        "odds": "1.90",
                        "name": "Odd"
                    },
                    {
                        "id": "2056370730",
                        "odds": "1.90",
                        "name": "Even"
                    }
                ]
            },
            "1st_quarter_winning_margin": {
                "id": "181247",
                "name": "1st Quarter Winning Margin",
                "odds": [
                    {
                        "id": "2056371490",
                        "odds": "8.00",
                        "header": "1",
                        "name": "1-2"
                    },
                    {
                        "id": "2056371491",
                        "odds": "8.50",
                        "header": "1",
                        "name": "3-4"
                    },
                    {
                        "id": "2056371492",
                        "odds": "10.00",
                        "header": "1",
                        "name": "5-6"
                    },
                    {
                        "id": "2056371497",
                        "odds": "12.00",
                        "header": "1",
                        "name": "7-8"
                    },
                    {
                        "id": "2056371498",
                        "odds": "15.00",
                        "header": "1",
                        "name": "9-10"
                    },
                    {
                        "id": "2056371503",
                        "odds": "8.50",
                        "header": "1",
                        "name": "11+"
                    },
                    {
                        "id": "2056371504",
                        "odds": "8.00",
                        "header": "2",
                        "name": "1-2"
                    },
                    {
                        "id": "2056371505",
                        "odds": "9.00",
                        "header": "2",
                        "name": "3-4"
                    },
                    {
                        "id": "2056371506",
                        "odds": "10.00",
                        "header": "2",
                        "name": "5-6"
                    },
                    {
                        "id": "2056371507",
                        "odds": "12.00",
                        "header": "2",
                        "name": "7-8"
                    },
                    {
                        "id": "2056371508",
                        "odds": "15.00",
                        "header": "2",
                        "name": "9-10"
                    },
                    {
                        "id": "2056371509",
                        "odds": "9.00",
                        "header": "2",
                        "name": "11+"
                    },
                    {
                        "id": "2056371510",
                        "odds": "13.00",
                        "name": "Tie"
                    }
                ]
            },
            "2nd_quarter_total_odd_even": {
                "id": "180171",
                "name": "2nd Quarter Total - Odd\/Even",
                "odds": []
            },
            "3rd_quarter_total_odd_even": {
                "id": "181366",
                "name": "3rd Quarter Total - Odd\/Even",
                "odds": []
            },
            "4th_quarter_total_odd_even": {
                "id": "181368",
                "name": "4th Quarter Total - Odd\/Even",
                "odds": []
            },
            "1st_quarter_player_rebounds": {
                "id": "181479",
                "name": "1st Quarter Player Rebounds",
                "odds": []
            },
            "1st_quarter_player_points": {
                "id": "181477",
                "name": "1st Quarter Player Points",
                "odds": []
            },
            "1st_quarter_player_assists": {
                "id": "181478",
                "name": "1st Quarter Player Assists",
                "odds": []
            }
        }
    },
    "schedule": {
        "updated_at": "1672325830",
        "key": "#AC#B18#C20604387#D48#E1453#F10#",
        "sp": {
            "main": [
                {
                    "id": "2049434755",
                    "odds": "1.90",
                    "name": "Spread",
                    "handicap": "+1.0"
                },
                {
                    "id": "2049434756",
                    "odds": "1.90",
                    "name": "Spread",
                    "handicap": "-1.0"
                },
                {
                    "id": "2049434762",
                    "odds": "1.90",
                    "name": "Total",
                    "handicap": "O 239.0"
                },
                {
                    "id": "2049434764",
                    "odds": "1.90",
                    "name": "Total",
                    "handicap": "U 239.0"
                },
                {
                    "id": "2049434758",
                    "odds": "2.00",
                    "name": "Money Line"
                },
                {
                    "id": "2049434760",
                    "odds": "1.83",
                    "name": "Money Line"
                }
            ]
        }
    },
    "team_props": {
        "updated_at": "1672325416",
        "key": "#AC#B18#C20604387#D19#E15942762#F19#I2#",
        "sp": {
            "team_with_highest_scoring_quarter": {
                "id": "181377",
                "name": "Team With Highest Scoring Quarter",
                "odds": [
                    {
                        "id": "2056373510",
                        "odds": "2.00",
                        "name": "1"
                    },
                    {
                        "id": "2056373511",
                        "odds": "2.05",
                        "name": "2"
                    },
                    {
                        "id": "2056373512",
                        "odds": "8.00",
                        "name": "Tie"
                    }
                ]
            },
            "team_totals": {
                "id": "181335",
                "name": "Team Totals",
                "odds": [
                    {
                        "id": "2056370735",
                        "odds": "1.86",
                        "header": "1",
                        "handicap": "Over 119.5"
                    },
                    {
                        "id": "2056370736",
                        "odds": "1.86",
                        "header": "1",
                        "handicap": "Under 119.5"
                    },
                    {
                        "id": "2056370733",
                        "odds": "1.90",
                        "header": "2",
                        "handicap": "Over 120.5"
                    },
                    {
                        "id": "2056370734",
                        "odds": "1.83",
                        "header": "2",
                        "handicap": "Under 120.5"
                    }
                ]
            },
            "alternative_team_totals": {
                "id": "181005",
                "name": "Alternative Team Totals",
                "odds": [
                    {
                        "id": "2056373462",
                        "odds": "1.03",
                        "header": "Over",
                        "name": "98.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373464",
                        "odds": "1.05",
                        "header": "Over",
                        "name": "100.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373466",
                        "odds": "1.08",
                        "header": "Over",
                        "name": "102.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373468",
                        "odds": "1.11",
                        "header": "Over",
                        "name": "104.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373470",
                        "odds": "1.15",
                        "header": "Over",
                        "name": "106.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373488",
                        "odds": "1.21",
                        "header": "Over",
                        "name": "108.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373463",
                        "odds": "9.50",
                        "header": "Under",
                        "name": "98.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373465",
                        "odds": "8.25",
                        "header": "Under",
                        "name": "100.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373467",
                        "odds": "7.00",
                        "header": "Under",
                        "name": "102.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373469",
                        "odds": "6.00",
                        "header": "Under",
                        "name": "104.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373471",
                        "odds": "4.75",
                        "header": "Under",
                        "name": "106.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373491",
                        "odds": "4.25",
                        "header": "Under",
                        "name": "108.5",
                        "team": "1"
                    },
                    {
                        "id": "2056373269",
                        "odds": "1.04",
                        "header": "Over",
                        "name": "99.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373273",
                        "odds": "1.06",
                        "header": "Over",
                        "name": "101.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373277",
                        "odds": "1.08",
                        "header": "Over",
                        "name": "103.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373279",
                        "odds": "1.11",
                        "header": "Over",
                        "name": "105.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373286",
                        "odds": "1.16",
                        "header": "Over",
                        "name": "107.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373291",
                        "odds": "1.22",
                        "header": "Over",
                        "name": "109.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373270",
                        "odds": "9.00",
                        "header": "Under",
                        "name": "99.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373274",
                        "odds": "8.00",
                        "header": "Under",
                        "name": "101.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373278",
                        "odds": "7.00",
                        "header": "Under",
                        "name": "103.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373280",
                        "odds": "5.75",
                        "header": "Under",
                        "name": "105.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373289",
                        "odds": "4.50",
                        "header": "Under",
                        "name": "107.5",
                        "team": "2"
                    },
                    {
                        "id": "2056373292",
                        "odds": "4.00",
                        "header": "Under",
                        "name": "109.5",
                        "team": "2"
                    }
                ]
            },
            "alternative_team_totals_2": {
                "id": "181085",
                "name": "Alternative Team Totals 2",
                "odds": []
            },
            "1st_quarter_team_totals": {
                "id": "181220",
                "name": "1st Quarter Team Totals",
                "odds": [
                    {
                        "id": "2056371046",
                        "odds": "2.00",
                        "header": "1",
                        "handicap": "Over 31.5"
                    },
                    {
                        "id": "2056371047",
                        "odds": "1.71",
                        "header": "1",
                        "handicap": "Under 31.5"
                    },
                    {
                        "id": "2056371154",
                        "odds": "1.83",
                        "header": "2",
                        "handicap": "Over 30.5"
                    },
                    {
                        "id": "2056371157",
                        "odds": "1.83",
                        "header": "2",
                        "handicap": "Under 30.5"
                    }
                ]
            },
            "alternative_1st_quarter_team_totals": {
                "id": "181221",
                "name": "Alternative 1st Quarter Team Totals",
                "odds": [
                    {
                        "id": "2056371048",
                        "odds": "1.04",
                        "header": "Over",
                        "name": "21.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371050",
                        "odds": "1.10",
                        "header": "Over",
                        "name": "23.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371052",
                        "odds": "1.20",
                        "header": "Over",
                        "name": "25.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371054",
                        "odds": "1.34",
                        "header": "Over",
                        "name": "27.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371056",
                        "odds": "1.57",
                        "header": "Over",
                        "name": "29.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371071",
                        "odds": "2.65",
                        "header": "Over",
                        "name": "33.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371049",
                        "odds": "8.75",
                        "header": "Under",
                        "name": "21.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371051",
                        "odds": "6.50",
                        "header": "Under",
                        "name": "23.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371053",
                        "odds": "4.30",
                        "header": "Under",
                        "name": "25.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371055",
                        "odds": "3.15",
                        "header": "Under",
                        "name": "27.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371058",
                        "odds": "2.25",
                        "header": "Under",
                        "name": "29.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371079",
                        "odds": "1.43",
                        "header": "Under",
                        "name": "33.5",
                        "team": "1"
                    },
                    {
                        "id": "2056371181",
                        "odds": "1.03",
                        "header": "Over",
                        "name": "20.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371196",
                        "odds": "1.07",
                        "header": "Over",
                        "name": "22.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371217",
                        "odds": "1.15",
                        "header": "Over",
                        "name": "24.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371247",
                        "odds": "1.28",
                        "header": "Over",
                        "name": "26.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371262",
                        "odds": "1.50",
                        "header": "Over",
                        "name": "28.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371299",
                        "odds": "2.40",
                        "header": "Over",
                        "name": "32.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371187",
                        "odds": "9.50",
                        "header": "Under",
                        "name": "20.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371198",
                        "odds": "7.50",
                        "header": "Under",
                        "name": "22.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371221",
                        "odds": "4.75",
                        "header": "Under",
                        "name": "24.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371250",
                        "odds": "3.50",
                        "header": "Under",
                        "name": "26.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371264",
                        "odds": "2.50",
                        "header": "Under",
                        "name": "28.5",
                        "team": "2"
                    },
                    {
                        "id": "2056371302",
                        "odds": "1.52",
                        "header": "Under",
                        "name": "32.5",
                        "team": "2"
                    }
                ]
            },
            "1st_half_team_totals": {
                "id": "181159",
                "name": "1st Half Team Totals",
                "odds": [
                    {
                        "id": "2056370853",
                        "odds": "1.86",
                        "header": "1",
                        "handicap": "Over 61.5"
                    },
                    {
                        "id": "2056370854",
                        "odds": "1.86",
                        "header": "1",
                        "handicap": "Under 61.5"
                    },
                    {
                        "id": "2056370877",
                        "odds": "1.86",
                        "header": "2",
                        "handicap": "Over 61.5"
                    },
                    {
                        "id": "2056370878",
                        "odds": "1.86",
                        "header": "2",
                        "handicap": "Under 61.5"
                    }
                ]
            },
            "alternative_1st_half_team_totals": {
                "id": "181160",
                "name": "Alternative 1st Half Team Totals",
                "odds": []
            },
            "1st_quarter_team_to_score_x_points": {
                "id": "181255",
                "name": "1st Quarter Team To Score X Points",
                "odds": []
            },
            "team_total_odd_even": {
                "id": "1731",
                "name": "Team Total - Odd\/Even",
                "odds": [
                    {
                        "id": "2056370661",
                        "odds": "1.90",
                        "header": "1",
                        "handicap": "Odd"
                    },
                    {
                        "id": "2056370662",
                        "odds": "1.90",
                        "header": "1",
                        "handicap": "Even"
                    },
                    {
                        "id": "2056370663",
                        "odds": "1.90",
                        "header": "2",
                        "handicap": "Odd"
                    },
                    {
                        "id": "2056370664",
                        "odds": "1.90",
                        "header": "2",
                        "handicap": "Even"
                    }
                ]
            },
            "1st_half_team_to_score_x_points": {
                "id": "181198",
                "name": "1st Half Team to Score X Points",
                "odds": [
                    {
                        "id": "2056370972",
                        "odds": "1.08",
                        "header": "Yes",
                        "name": "50",
                        "team": "1"
                    },
                    {
                        "id": "2056370973",
                        "odds": "8.25",
                        "header": "No",
                        "name": "50",
                        "team": "1"
                    },
                    {
                        "id": "2056370978",
                        "odds": "1.08",
                        "header": "Yes",
                        "name": "50",
                        "team": "2"
                    },
                    {
                        "id": "2056370979",
                        "odds": "8.25",
                        "header": "No",
                        "name": "50",
                        "team": "2"
                    }
                ]
            }
        }
    }
}

def get_decisions(request):
    decisions = []
    bet365_api_base_path = 'https://api.b365api.com'
    basketball_sport_id = 18
    nba_league_id = 10041830
    upcoming_events_request_url = bet365_api_base_path + '/v1/bet365/upcoming'
    upcoming_events_request_params = {
        'token': BET365_API_TOKEN,
        'sport_id': basketball_sport_id,
        'league_id': nba_league_id,
        'skip_esports': True
    }
    # upcoming_events_response = requests.get(upcoming_events_request_url, params=upcoming_events_request_params)
    # events = upcoming_events_response.json()['results']

    driver_options = ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver = uc.Chrome(driver_options)
    driver.get('https://www.fantasypros.com/daily-fantasy/nba/defense-vs-position.php')
    defense_position_table_pts_column = driver.find_element(By.XPATH, '//*[@id="data-table"]/thead/tr/th[2]/div')
    defense_position_table_pts_column.click()
    defense_position_table_pts_column.click()
    defense_position_table = driver.find_element(By.XPATH, '//*[@id="data-table"]')
    defense_position_table_content = defense_position_table.get_attribute('outerHTML')
    defense_position_table_df = pd.read_html(defense_position_table_content)[0]
    defense_position_table_team_points_columns = defense_position_table_df[['Team', 'PTS']]

    driver.get('https://statmuse.com/nba')

    for event in events:
        decision ={
            'event_id': event['id'],
            'home_team': event['home']['name'],
            'away_team': event['away']['name'],
            'entries': []
        }
        prematch_odds_request_url = bet365_api_base_path + '/v3/bet365/prematch'
        prematch_odds_request_params = {
            'token': BET365_API_TOKEN,
            'FI': event['id']
        }
        # prematch_odds_response = requests.get(prematch_odds_request_url, params=prematch_odds_request_params)
        # odds = prematch_odds_response.json()['results'][0]
        player_points_odds = odds['player_props']['sp']['player_points']['odds']

        for odd in player_points_odds:
            if odd['header'] == 'Over':
                search_input = driver.find_element(By.NAME, 'question[query]')
                search_input.send_keys(odd['name'])
                search_input.send_keys(Keys.ENTER)

                time.sleep(2)

                next_game_table_node = driver.find_element(By.XPATH, '/html/body/div[6]/player-profile/div/div[2]/div[2]/div[2]/table')
                next_game_table_content = next_game_table_node.get_attribute('outerHTML')
                next_game_table_df = pd.read_html(next_game_table_content)[0]
                player_last_five_games_points_per_game = next_game_table_df['PPG'][0]
                home_away_points_per_game = next_game_table_df['PPG'][1]
                stats_table_node = driver.find_element(By.XPATH, '/html/body/div[6]/player-profile/div/div[2]/div[3]/div[2]/table')
                stats_table_content = stats_table_node.get_attribute('outerHTML')
                stats_table_df = pd.read_html(stats_table_content)[0]
                player_current_season_points_per_game = stats_table_df['PPG'][0]
                opponent_team_name = event['home']['name'] if odd['name2'] == event['away']['name'] else event['away']['name']

                location_key = 'home_average' if odd['name2'] == event['home']['name'] else 'away' + '_average'
                decision['entries'].append({
                    'player': odd['name'],
                    'market': 'Over Points',
                    'line': odd['handicap'],
                    '2022-23_average': player_current_season_points_per_game,
                    location_key: home_away_points_per_game,
                    'last_5_games_average': player_last_five_games_points_per_game,
                    'bet': 0.75
                })
        
        decisions.append(decision)

    driver.quit()

    return HttpResponse(json.dumps(decisions))
