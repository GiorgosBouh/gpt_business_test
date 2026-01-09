from questionnaire_storage import QuestionnaireStorage


def test_add_and_list_responses(tmp_path) -> None:
    storage_path = tmp_path / "responses.csv"
    storage = QuestionnaireStorage(storage_path=storage_path)
    storage.add_response({"name": "Ada"})

    assert storage.list_responses() == [{"name": "Ada"}]

