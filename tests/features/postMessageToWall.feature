Feature: postMessageToWall
    Testing VK api
    Scenario: postMessageToWall
        Given Request string to vk api
        When I make query request by get
        Then I should receive post_id
        And It must be a digit