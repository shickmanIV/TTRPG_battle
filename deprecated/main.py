from Classes import Class, AbilityType
from Spells import spell
from Game import Actor

def getPaths1():
    url = "https://www.dnd5eapi.co"
    headers = {'Accept': 'application/json'}
    path = "/api/ability-scores/cha"
    paths = []
    response = requests.get(url + path, headers=headers)

    if response.status_code == 200:
        form_data = response.json()

        for item in form_data['skills']:
            paths.append(item['url'])

        for i in paths:
            print(i)

def getPaths2():
    url = "https://www.dnd5eapi.co"
    headers = {'Accept': 'application/json'}
    path = "/api/features"
    response = requests.get(url + path, headers=headers)
    if response.status_code == 200:
        form_data = response.json()
        print(form_data)
        classes = form_data['results']
    
    for item in classes:
        print(item)

def make_graphql_query(query, url):
    headers = {'Content-Type': 'application/json',}
    data = {'query': query}
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def example_graphql_query():
    # Example GraphQL query: fetches each class and their corresponding hit die.
    graphql_query = """
    {
      classes {
        name
        hit_die
      }
    }
    """

    # Example GraphQL endpoint URL
    graphql_endpoint = 'https://www.dnd5eapi.co/graphql'

    # Make the GraphQL query
    result = make_graphql_query(graphql_query, graphql_endpoint)

    if 'data' in result and 'classes' in result['data']:
        for item in result['data']['classes']:
            if 'name' and 'hit_die' in item:
                print(item['name'], ':', item['hit_die'])

    if 'data' in result and 'skills' in result['data']:
        for item in result['data']['skills']:
            if 'name' in item:
                print(item['name'])

def get_core_classes():
    graphql_query = """ {
        classes {
            name
            hit_die
            index
            multi_classing {
                prerequisites {
                    minimum_score
                    ability_score {
                        name
                    }
                }
            }
            proficiencies {
                name
            }
            proficiency_choices {
                choose
                from {
                    options {
                        ... on ProficiencyReferenceOption {
                            item {
                                name
                            }
                        }
                    }
                }
            }
            saving_throws {
                name
            }
            spellcasting {
                level
                spellcasting_ability {
                    name
                }
            }
            starting_equipment {
                quantity
                equipment {
                    name
                }
            }
            starting_equipment_options {
                choose
                from {
                    ... on EquipmentCategoryOptionSet {
                        equipment_category {
                            name
                        }
                    }
                    ... on EquipmentOptionSet {
                        options {
                            ... on CountedReferenceOption {
                                count
                                of {
                                    name
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    """
    graphql_endpoint = 'https://www.dnd5eapi.co/graphql'
    result = make_graphql_query(graphql_query, graphql_endpoint)

    print(result)
    

if __name__ == "__main__":
    baseActor = Actor()
    print(baseActor)