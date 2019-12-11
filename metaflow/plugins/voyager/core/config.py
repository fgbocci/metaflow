def _fury_token():
    return "f53a228cd4d304d27296af41ac03dbbcdad186e75e0cf2271bbe97eed633b432"


def _git_token():
    return "261326d101952a595700156bcf5af82bdae70c1e"


CONFIG = {
    "DEV": {
        "etl": {"endpoint": "http://api.furycloud.io/applications/{}/etls/{}"},
        "training": {
            "endpoint": "http://api.furycloud.io/applications/{}/trainings/{}"
        },
        "voyager": {"launch_tasks": "prod.voyager.melifrontends.com/launch_tasks"},
        "jenkins": {
            "logs": "http://data-apps-pipeline.furycloud.io/blue/organizations/jenkins/{}/detail/{}/{}/pipeline"
        },
        "alert": {
            "opsgenie": "http://api.opsgenie.com/v2/alerts",
            "mail": "http://api.internal.ml.com/bi/send_mail",
        },
        "fury_token": _fury_token(),
        "git_token": _git_token(),
    },
    "PROD": {
        "etl": {"endpoint": "http://api.furycloud.io/applications/{}/etls/{}"},
        "training": {
            "endpoint": "http://api.furycloud.io/applications/{}/trainings/{}"
        },
        "voyager": {"launch_tasks": "prod.voyager.melifrontends.com/launch_tasks"},
        "jenkins": {
            "logs": "http://data-apps-pipeline.furycloud.io/blue/organizations/jenkins/{}/detail/{}/{}/pipeline"
        },
        "alert": {
            "opsgenie": "http://api.opsgenie.com/v2/alerts",
            "mail": "http://internal.mercadolibre.com/bi/send_mail",
        },
        "fury_token": _fury_token(),
        "git_token": _git_token(),
    },
}
