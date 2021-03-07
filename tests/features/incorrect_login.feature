Feature: IncorrectAuth
    Testing VK api
    Scenario: incorrect_login
        Given Request string to vk api
        When I make query request by get
        And Put wrong service token
        Then I should not receive status 200