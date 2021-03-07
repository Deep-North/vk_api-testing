Feature: postMessageToWallWithEmptyMessage
    Testing VK api
    Scenario: postMessageToWallWithEmptyMessage
        Given Request string to vk api
        When I make query request by get
        Then I should receive error 100


