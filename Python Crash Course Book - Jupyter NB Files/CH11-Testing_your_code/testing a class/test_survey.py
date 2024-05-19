import pytest
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
    

def test_store_3_responses():
    '''test to check 3 responses are stored properly'''
    question = 'What language you like?'

    survey3 = AnonymousSurvey(question)
    responses = ['english', 'hindi', 'french']

    for resp in responses:
        survey3.store_response(resp)

    for resp in responses:
        assert resp in survey3.responses



# we are creating multiple instances of class
# In testing, a fixture helps set up a test environment. Often, this means creating a resource that’s used by more than one test. 

# decorator: @pytest.fixture

# fixture can used to single instance that can be used in multiple test functions

@pytest.fixture
def common_survey():
    '''return instance that can be used in other functions'''
    question = 'what language you like?'
    inctanceCreated = AnonymousSurvey(question)
    return inctanceCreated

def test_one_resp(common_survey):       #passing fixture def to test functions
    lang = 'english'
    common_survey.store_response(lang)

    assert lang in common_survey.responses