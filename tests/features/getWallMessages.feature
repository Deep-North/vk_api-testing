Feature: getWallMessages
    Testing VK api
    Scenario: getWallMessages
        Given Request string to vk api
        When I make query request by get
        Then I should receive messages from wall
        And It count must be greater or equal 0