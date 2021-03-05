Feature: Auth
    Testing VK api
    Scenario: login
        Given Request string to vk api
        When I make query request by get
        Then I should receive status 200