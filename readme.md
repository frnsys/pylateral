# Lateral

This is a Python interface to [Lateral](https://lateral.io/)'s APIs.

The package currently only supports their [Recommender API](https://developers.lateral.io/docs/services/546b2cc23705a70f4cd2766d/operations/546b2e053705a70f4cd2766e).

## Installation

    $ pip install lateral

## Usage

    from lateral.api import LateralRecommender
    lr = LateralRecommender('my-subscription-key')

    text = '''European leaders expressed their desire to support the recovery as the global economy moves beyond the global financial crisis. European Commission President Barroso and European Council President Van Rompuy stressed the importance of coordinated growth strategies as well as finalising agreements on core financial reforms, and actions on tax and anti-corruption.'''

    doc_id = lr.add_doc(text)

    doc = lr.fetch_doc(doc_id)

    lr.delete_doc(doc_id)