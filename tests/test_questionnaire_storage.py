from questionnaire_storage import QuestionnaireStorage


def test_add_and_list_responses() -> None:
    storage = QuestionnaireStorage()
    storage.add_response({"name": "Ada"})

    assert storage.list_responses() == [{"name": "Ada"}]
