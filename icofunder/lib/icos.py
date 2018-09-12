#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.utils.translation import ugettext as _

ICOS = {
    "ongoing": [
        {
            "rightmesh": {
                "name": "RightMesh",
                "logo": "rightmesh.png",
                "desc": _("""RightMesh 是一款基于软件的ad hoc 移动网状网络平台和协议，使用区块链技术和MESH令牌来推动增长。"""),
                "start_at": "",
                "ended_at": "2018-06-13",
                "video": "rightmesh.mp4",
                "website": "https://www.rightmesh.io/",
                "whitepaper": "rightmesh.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 5.0,
                    "team": 4.2,
                    "vision": 4.3,
                    "product": 4.5,
                    "rating": 4.5,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("中等利润"),
                },
                "token": {
                    "name": "RMESH",
                    "type": "ERC20",
                    "total": "129,498,559",
                    "sale": "38,850,000 RMESH (30%)",
                    "goal": "$30,000,000",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "CANADA, USA",
                    "price": "1 MESH = 1.00 USD",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH",
                    "cash_at": "",
                    "exchange_at": "",
                },
                "socials": {
                    "facebook": "https://www.facebook.com/TheRightMesh/",
                    "twitter": "https://twitter.com/Right_Mesh",
                    "instagram": "https://www.instagram.com/rightmesh/",
                    "linkedin": "https://www.linkedin.com/company/right-mesh",
                    "github": "https://github.com/rightmesh",
                    "medium": "https://medium.com/rightmesh",
                    "telegram": "https://t.me/RightMesh_Official",
                },
            }
        },
        {
            "cardstack": {
                "name": "CardStack",
                "logo": "cardstack.jpg",
                "desc": _("""区块链服务
分散式互联网的体验层。Cardstack 是一个开源框架和共识协议，它使区块链可用于大众市场并扩展，创建了一个分散的软件生态系统，可以挑战当今的数字超级大国。"""),
                "start_at": "",
                "ended_at": "2018-05-30",
                "video": "cardstack.mp4",
                "website": "http://cardstack.io/",
                "whitepaper": "cardstack.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 4.7,
                    "team": 4.0,
                    "vision": 4.6,
                    "product": 4.2,
                    "rating": 4.3,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("中等利润"),
                },
                "token": {
                    "name": "CARD",
                    "type": "ERC20",
                    "total": "6,000,000,000",
                    "sale": "40%",
                    "goal": "$35,000,000",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "USA",
                    "price": "1 CARD = 0.0175 USD",
                    "bonus": "10%",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH",
                    "cash_at": "",
                    "exchange_at": "",
                },
                "socials": {
                    "twitter": "https://twitter.com/cardstack",
                    "medium": "https://medium.com/cardstack",
                    "telegram": "https://telegram.me/cardstack",
                    "github": "https://github.com/cardstack/cardstack",
                }
            }
        },
    ],
    "upcoming": [
        {
            "orvium": {
                "name": "Orvium",
                "logo": "orvium.jpg",
                "desc": _("""开放和透明的科学由区块链支持
Orvium 是第一个管理学术刊物的生命周期和相关数据的开源和分散框架。"""),
                "start_at": "",
                "ended_at": "",
                "video": "orvium.mp4",
                "website": "http://orvium.io/",
                "whitepaper": "orvium.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 4.6,
                    "team": 3.9,
                    "vision": 4.4,
                    "product": 4.2,
                    "rating": 4.2,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("中等利润"),
                },
                "token": {
                    "name": "ORV",
                    "type": "ERC20",
                    "total": "379,000,000",
                    "sale": "60%",
                    "goal": "$20,000,000",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "China, Singapore, Canada",
                    "price": "1 ORV = 0.1 USD",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH",
                    "cash_at": "",
                    "exchange_at": "",
                },
                "socials": {
                    "twitter": "https://twitter.com/orvium",
                    "reddit": "https://www.reddit.com/r/Orvium/",
                    "bitcointalk": "https://bitcointalk.org/index.php?topic=3535259.0",
                    "facebook": "https://www.facebook.com/orvium.io",
                    "linkedin": "https://www.linkedin.com/company/orvium",
                    "medium": "https://medium.com/@orvium",
                    "instagram": "https://www.instagram.com/orvium/",
                    "telegram": "https://t.me/orvium",
                }
            }
        },
        {
            "skillchain": {
                "name": "SkillChain ICO",
                "logo": "skillchain.svg",
                "desc": _(
                    """区块链上的技能认证
SkillChain 是大学、公司和非学术培训公司永久性认证，可以保证您的技能而制定的权威性议定书。"""
                ),
                "start_at": "2018-09-01",
                "ended_at": "2018-12-30",
                "video": "skillchain.mp4",
                "website": "https://www.skillchain.io/",
                "whitepaper": "skillchain.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 4.9,
                    "team": 2.9,
                    "vision": 2.5,
                    "product": 2.5,
                    "rating": 3.8,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("中等利润"),
                },
                "token": {
                    "name": "SKI",
                    "type": "ERC20",
                    "total": "190,800,000",
                    "sale": "",
                    "goal": "11,000 ETH",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "USA",
                    "price": "",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH",
                    "cash_at": "",
                    "exchange_at": "",
                },
                "socials": {
                    "facebook": "https://www.facebook.com/Skillchain/",
                    "linkedin": "https://www.linkedin.com/company/skillchain",
                    "bitcointalk": "https://bitcointalk.org/index.php?topic=3039181",
                    "medium": "http://www.medium.com/@Skillchain",
                    "twitter": "https://twitter.com/skillchain_io",
                    "reddit": "https://www.reddit.com/user/skillchain",
                    "telegram": "https://t.me/SkillchainOFFICIAL",
                },
            }
        },

    ],
    "ended": [
        {
            "gochain1": {
                "name": "GoChain Public Sale",
                "logo": "gochain.jpg",
                "desc": _("""GoChain 是一款可扩展，高性能，低成本，分散式的加密货币和区块链，支持智能合约和分布式应用程序。"""),
                "start_at": "2018-05-16",
                "ended_at": "2018-05-31",
                "video": "",
                "image": "gochain.png",
                "website": "https://gochain.io/",
                "whitepaper": "gochain.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 5.0,
                    "team": 4.4,
                    "vision": 4.6,
                    "product": 4.7,
                    "rating": 4.7,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("高等利润"),
                },
                "token": {
                    "name": "GOC",
                    "type": "ERC20",
                    "total": "1,000,000,000",
                    "sale": "50%",
                    "goal": "$13,500,000",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "CANADA, USA",
                    "price": "1ETH = 16,000 GOC",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH",
                    "cash_at": "",
                    "exchange_at": "",
                },
                "socials": {
                    "twitter": "https://twitter.com/go_chain",
                    "medium": "https://medium.com/gochain",
                    "telegram": "https://t.me/go_chain",
                    "facebook": "https://www.facebook.com/gochaingo",
                    "reddit": "https://www.reddit.com/r/OfficialGoChain/",
                    "bitcointalk": "https://bitcointalk.org/index.php?topic=2976243.msg30582557",
                },
            }
        },
        {
            "gochain": {
                "name": "GoChain Pre-Sale",
                "logo": "gochain.jpg",
                "desc": _("""GoChain 是一款可扩展，高性能，低成本，分散式的加密货币和区块链，支持智能合约和分布式应用程序。"""),
                "start_at": "",
                "ended_at": "2018-05-02",
                "video": "",
                "image": "gochain.png",
                "website": "https://gochain.io/",
                "whitepaper": "gochain.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 5.0,
                    "team": 4.4,
                    "vision": 4.6,
                    "product": 4.7,
                    "rating": 4.7,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("高等利润"),
                },
                "token": {
                    "name": "GOC",
                    "type": "ERC20",
                    "total": "1,000,000,000",
                    "sale": "50%",
                    "goal": "$13,500,000",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "CANADA, USA",
                    "price": "1ETH = 20,000 GOC",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH",
                    "cash_at": "",
                    "exchange_at": "",
                },
                "socials": {
                    "twitter": "https://twitter.com/go_chain",
                    "medium": "https://medium.com/gochain",
                    "telegram": "https://t.me/go_chain",
                    "facebook": "https://www.facebook.com/gochaingo",
                    "reddit": "https://www.reddit.com/r/OfficialGoChain/",
                    "bitcointalk": "https://bitcointalk.org/index.php?topic=2976243.msg30582557",
                },
            }
        },
        {
            "skillchain-pre": {
                "name": "SkillChain Pre-ICO",
                "logo": "skillchain.svg",
                "desc": _(
                    """区块链上的技能认证
SkillChain 是大学、公司和非学术培训公司永久性认证，可以保证您的技能而制定的权威性议定书。"""
                ),
                "start_at": "2018-04-06",
                "ended_at": "2018-04-25",
                "video": "skillchain.mp4",
                "website": "https://www.skillchain.io/",
                "whitepaper": "skillchain.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 4.9,
                    "team": 2.9,
                    "vision": 2.5,
                    "product": 2.5,
                    "rating": 3.8,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("中等利润"),
                },
                "token": {
                    "name": "SKI",
                    "type": "ERC20",
                    "total": "190,800,000",
                    "sale": "30%",
                    "goal": "3,000 ETH",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "USA",
                    "price": "1 ETH = 5040 SKI",
                    "bonus": "20%",
                    "accepts": "Ethereum",
                    "limit": "0.1",
                    "cash_at": "",
                    "exchange_at": "",
                },
                "socials": {
                    "facebook": "https://www.facebook.com/Skillchain/",
                    "linkedin": "https://www.linkedin.com/company/skillchain",
                    "bitcointalk": "https://bitcointalk.org/index.php?topic=3039181",
                    "medium": "http://www.medium.com/@Skillchain",
                    "twitter": "https://twitter.com/skillchain_io",
                    "reddit": "https://www.reddit.com/user/skillchain",
                    "telegram": "https://t.me/SkillchainOFFICIAL",
                },
            }
        },
        {
            "telcoin": {
                "name": "TelCoin",
                "logo": "telcoin.png",
                "desc": _(
                    """全球范围内整合加密货币与移动网络。
Telcoin专注于与全球移动网络连接，实现电信移动资金，预付信用和后付费计费平台之间的轻松转换。"""
                ),
                "start_at": "2017-12-12",
                "ended_at": "2017-12-31",
                "video": "telcoin.mp4",
                "website": "https://www.telco.in/",
                "whitepaper": "telcoin.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 4.2,
                    "team": 4.7,
                    "vision": 4.3,
                    "product": 4.0,
                    "rating": 4.3,
                },
                "ratings": {
                    "hype": _("高"),
                    "risk": _("正常"),
                    "roi": _("高"),
                    "score": _("中等利润"),
                },
                "token": {
                    "name": "TELCOIN",
                    "type": "ERC20",
                    "total": "100,000,000,000",
                    "sale": "20%",
                    "goal": "25,000,000 USD",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "USA",
                    "price": "1 TELCOIN = 0.0013 USD",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH/NO",
                    "cash_at": "",
                    "exchange_at": "2018-01-14",
                },
                "socials": {
                    "facebook": "https://www.facebook.com/telcoin/",
                    "bitcointalk": "https://bitcointalk.org/index.php?topic=2387659.0",
                    "twitter": "https://twitter.com/telcoin_team",
                    "telegram": "https://t.me/telcoincommunity",
                    "medium": "https://medium.com/@telcoin",
                    "reddit": "https://www.reddit.com/r/Telcoin/",
                    "github": "https://github.com/telcoin",
                    "youtube": "https://www.youtube.com/channel/UCBEKBh64cZy7U3O7VtKsLOg",
                },
            }
        },
        {
            "zilliqa": {
                "name": "Zilliqa",
                "logo": "zilliqa.png",
                "desc": _(
                    """Zilliqa - 下一代高吞吐量区块链平台。
Zilliqa 是一个新的区块链平台，旨在安全地扩展开放，权限较小的分布式网络。 使 Zilliqa 可扩展的核心功能是分割 - 将网络分割为几个能够并行处理事务的小型组件网络（称为碎片）。"""
                ),
                "start_at": "2017-12-27",
                "ended_at": "2018-01-04",
                "video": "zilliqa.mp4",
                "website": "https://www.zilliqa.com/",
                "whitepaper": "zilliqa.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 4.6,
                    "team": 4.7,
                    "vision": 4.4,
                    "product": 4.6,
                    "rating": 4.5,
                },
                "ratings": {
                    "hype": _("高"),
                    "risk": _("正常"),
                    "roi": _("高"),
                    "score": _("高等利润"),
                },
                "token": {
                    "name": "ZIL",
                    "type": "ERC20",
                    "total": "21,000,000,000",
                    "sale": "30%",
                    "goal": "22,000,000 USD",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "USA, CHINA, JAPAN",
                    "price": "1 ZIL = 0.0038 USD",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "2 ETH / 5 ETH",
                    "cash_at": "",
                    "exchange_at": "2018-01-14",
                },
                "socials": {
                    "twitter": "https://twitter.com/zilliqa",
                    "reddit": "https://www.reddit.com/r/zilliqa/",
                    "slack": "https://invite.zilliqa.com/",
                    "youtube": "https://www.youtube.com/channel/UCvinnFbf0u71cajoxKcfZIQ",
                    "telegram": "https://t.me/zilliqachat",
                    "github": "https://github.com/Zilliqa/Zilliqa",
                },
            }
        },

        {
            "aidcoin": {
                "name": "AidCoin",
                "logo": "aidcoin.jpg",
                "desc": _(
                    """AidCoin 是 ERC20 令牌，旨在成为通过以太坊区块链透明捐赠的首选方法。
AID 令牌将为 AIDChain 提供动力，AIDChain 是一个通过易于使用的界面提供服务生态系统的平台，连接非营利性社区，同时实现捐赠的完全透明和可追踪性。AIDChain 的服务包括内部交换，将主要加密货币转换为 AidCoin，一个内置钱包用于存储和捐赠，透明地跟踪捐赠的投资者，将捐赠者与非营利部门所有参与者以及智能模板连接起来的工具合同开展筹款活动。"""
                ),
                "start_at": "2018-01-16",
                "ended_at": "2018-01-16",
                "video": "aidcoin.mp4",
                "website": "https://www.aidcoin.co/",
                "whitepaper": "aidcoin.pdf",
                "platform": "Ethereum",
                "buy_with": "Ethereum",
                "level": {
                    "profile": 4.2,
                    "team": 3.8,
                    "vision": 4.1,
                    "product": 4.3,
                    "rating": 4.1,
                },
                "ratings": {
                    "hype": _("正常"),
                    "risk": _("正常"),
                    "roi": "",
                    "score": _("中等利润"),
                },
                "token": {
                    "name": "AID",
                    "type": "ERC20",
                    "total": "100,000,000",
                    "sale": "3,865,900 USD（8333 ETH）",
                    "goal": "18,600,000 USD（14,333 ETH）",
                    "whitelist": "YES",
                    "kyc": "YES",
                    "participate": "USA",
                    "price": "1 ETH = 2,000 AID",
                    "bonus": "",
                    "accepts": "Ethereum",
                    "limit": "0.1 ETH",
                    "cash_at": "",
                    "exchange_at": "2018-01-25",
                },
                "socials": {
                    "twitter": "https://twitter.com/aid_coin",
                    "facebook": "https://www.facebook.com/AidCoinCo/",
                    "reddit": "https://www.reddit.com/r/AidCoin/",
                    "bitcointalk": "https://bitcointalk.org/index.php?topic=2347477.0",
                    "medium": "https://medium.com/aidcoin",
                    "discord": "https://discordapp.com/invite/aubRWRT",
                    "telegram": "https://t.me/aidcoincommunity",
                },
            }
        },

    ]
}

PROJECTS = {}
for ico in ICOS['ongoing']:
    PROJECTS[ico.keys()[0]] = ['ongoing', ICOS['ongoing'].index(ico)]
for ico in ICOS['upcoming']:
    PROJECTS[ico.keys()[0]] = ['upcoming', ICOS['upcoming'].index(ico)]
for ico in ICOS['ended']:
    PROJECTS[ico.keys()[0]] = ['ended', ICOS['ended'].index(ico)]
