<p align="center" dir="auto"><a href="https://retroachievements.org" rel="nofollow"><img src="https://raw.githubusercontent.com/RetroAchievements/RAWeb/master/public/assets/images/ra-icon.webp" width="200" alt="RetroAchievements Logo" style="max-width: 100%;"></a></p>

<h1 align="center">retroachievements-api</h1>

<p align="center">
  <i>A Python library that lets you get achievement, user, and game data from RetroAchievements.</i>
  <br /><br />
</p>

<p align="center">
  <a href="https://api-docs.retroachievements.org/getting-started.html"><strong>Documentation: Get Started</strong></a>
  <br />
</p>

<hr />

## Status
This library is currently a work in progress, endpoint and test coverage can be found below:

ℹ️ &nbsp;Endpoint coverage: 8 of 30  
ℹ️ &nbsp;Test coverage: 0 of 30

## Features

✅ &nbsp;Officially-supported, aligns 1:1 with the RAWeb API.  
✅ &nbsp;Backwards-compatible, easy migration path to API v2.  
✅ &nbsp;Supports Python 3.11+.

<hr />

## Documentation

Learn how to authenticate and start pulling data from RetroAchievements on our documentation website.

- [Get started](https://api-docs.retroachievements.org/getting-started.html)
- [Get a user's profile information](https://api-docs.retroachievements.org/v1/users/get-user-summary.html)
- [Look up games a user has completed](https://api-docs.retroachievements.org/v1/users/get-user-completed-games.html)
- [Get a game's metadata](https://api-docs.retroachievements.org/v1/games/get-game-extended.html)

## Installation

Coming Soon
## How to begin making API calls

To use any endpoint function in the API, you must first be authorized by RetroAchievements. Fortunately, this is a fairly straightforward process.

1. Visit [your control panel](https://retroachievements.org/controlpanel.php) on the RA website.

2. Find the "Keys" section on the page. Copy the web API key value. **Do not expose your API key anywhere publicly.**

3. You can now create your authorization object using your web API key.

```python
from retroachievements import RAClient

userName = '<your username on RA>'
webApiKey = '<your web API key>'

auth = RAClient(userName, webApiKey)
```

4. You now have all you need to use any function in the API. Each function takes this authorization object as its first argument. Here's an example:

```python
from retroachievements import getGame

// This returns basic metadata about the game on this page:
// https://retroachievements.org/game/14402
game = auth.getGame(14402);
```

## Contributing

See [Contribution Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## Security Vulnerabilities

Please review [our security policy](../../security/policy).

## Credits

- [All Contributors](../../contributors)

## License

MIT License (MIT). See [License File](LICENSE.md).
