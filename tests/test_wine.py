from sqlalchemy import select

from wine_project.models.models import Wine, EvaluatedWines


def test_create_wine_record(session):
    new_wine = Wine(
        fixed_accidity = 1,
        volatile_acidity = 1,
        citric_acid = 1,
        residual_sugar = 1,
        chlorides = 1,
        free_sulfur_dioxide = 1,
        total_sulfur_dioxide = 1,
        density = 1,
        pH = 1,
        sulphates = 1,
        alcohol = 1,
    )
    session.add(new_wine)
    session.commit()

    wine = session.scalar(select(Wine).where(Wine.id == '1'))

    assert wine.id == 1

def test_create_evaluation(session):

    new_wine = Wine(
        fixed_accidity = 1,
        volatile_acidity = 1,
        citric_acid = 1,
        residual_sugar = 1,
        chlorides = 1,
        free_sulfur_dioxide = 1,
        total_sulfur_dioxide = 1,
        density = 1,
        pH = 1,
        sulphates = 1,
        alcohol = 1,
    )
    new_eval = EvaluatedWines(
        wine = new_wine,
        quality = 5
    )
    session.add(new_wine)
    session.add(new_eval)
    session.commit()

    eval = session.scalar(select(EvaluatedWines).where(EvaluatedWines.id == '1'))

    assert eval.id == 1