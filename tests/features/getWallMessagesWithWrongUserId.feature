Feature: getWallMessagesWithWrongUserId
    Testing VK api
    Scenario: getWallMessagesWithWrongUserId
        Given Request string to vk api
        When I make query request by get
        Then I should receive error 100