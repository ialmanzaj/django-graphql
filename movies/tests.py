import graphene
import json

from django.test.testcases import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from .schema import Query
from .models import Movie


class MovieTestCase(TestCase):

    def test_movies_exist(self):
        entry = Movie(name="Titanic")
        self.assertEqual(str(entry), entry.name)

""" class MyFancyTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema

    def test_some_query(self):
        response = self.query(
            '''
            query {
                myModel {
                    id
                    name
                }
            }
            ''',
            op_name='myModel'
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
        

    def test_query_with_variables(self):
        response = self.query(
            '''
            query myModel($id: Int!){
                myModel(id: $id) {
                    id
                    name
                }
            }
            ''',
            op_name='myModel',
            variables={'id': 1}
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
        

    def test_some_mutation(self):
        response = self.query(
            '''
            mutation myMutation($input: MyMutationInput!) {
                myMutation(input: $input) {
                    my-model {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='myMutation',
            input_data={'my_field': 'foo', 'other_field': 'bar'}
        )

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response) """