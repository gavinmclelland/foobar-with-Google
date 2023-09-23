<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gavinmclelland/foobar-with-Google">
    <img src="images/logo.svg" alt="Logo" width="130" height="120">
  </a>

<h3 align="center">Google Foobar version 20230817-beta</h3>

  <p align="center">
    This repository contains my solutions and journey documentation for Google Foobar version 20230817-beta challenges. Focused on Python solutions and educational sharing. Work in progress.
    <br />
    <a href="https://github.com/gavinmclelland/foobar-with-Google/challenge-journal"><strong>Explore my Challenge Journal »</strong></a>
    <br />
    <br />
    <a href="https://foobar.withgoogle.com/">foo.bar</a>
    ·
    <a href="https://github.com/gavinmclelland/foobar-with-Google/issues">Report Bug</a>
    ·
    <a href="https://github.com/gavinmclelland/foobar-with-Google/issues">Provide Feedback</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#constraints">Constraints</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# I Foobar, with Google

[![Google Foobar Screen Shot][product-screenshot]](https://foobar.withgoogle.com)

Google Foobar is an invitation-only coding challenge created by Google. It features five levels of progressively difficult programming problems. The challenges cover a wide array of algorithmic topics, including but not limited to:

- **Graph Theory**
- **Dynamic Programming**
- **String Manipulation**
- **Data Structures**
- **Recursion**
- **Sorting**
- **Optimization**
- **Mathematical Puzzles**

### My Google Foobar Status

| Current level | Challenges left to complete level |
|---------------|----------------------------------|
| 2             | 2                                |

- [x] Level 1: 100% [==========================================]
    - [x] [Skipping Work](challenge-journal/level1-skipping-work)
- [ ] Level 2: 0% [..........................................]
    - [ ] Challenge 2a TBD
    - [ ] Challenge 2b TBD
- [ ] Level 3: 0% [..........................................]
- [ ] Level 4: 0% [..........................................]
- [ ] Level 5: 0% [..........................................]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Google][Google]][google-url]
* [![visualstudiocode][visualstudiocode]][visualstudiocode-url]
* [![Docker][Docker]][docker-url]
* [![Python][Python]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Since the solution is designed to run in a sandboxed environment by calling the `solution()` function, running it outside of this context won't be applicable.

### Prerequisites

* Python 2.7.13 sandbox.
  * All tests will be run by calling the solution() function.

  * Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

  * Input/output operations are not allowed.

  * solution must be under 32000 characters in length including new lines and other non-printing characters.

### Constraints

All Foobar challenge solutions must adhere to the constraints specified in `constraints.txt`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. Login to foo.bar with Google [https://foobar.withgoogle.com/](https://foobar.withgoogle.com/)

2. Clone the repo
   ```sh
   git clone https://github.com/gavinmclelland/foobar-with-Google.git
   ```
3. In Google Foobar, run tests on solution files [solution.py]
   ```sh
   verify solution.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
- [ ] Reach 100% for all 5 levels of Google Foobar
- [ ] Foobar Python 2.7.13 sandbox-quick-start for Apple Silicon
    - [ ] Dockerfile
    - [ ] .devcontainer for VS Code

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. While this repository at [github.com/gavinmclelland/foobar-with-Google](https://github.com/gavinmclelland/foobar-with-Google) primarily documents my personal journey through Google Foobar challenges, contributions that enhance the educational value or optimize the existing solutions are **greatly appreciated**.

**Note**: The main solutions to the challenges will remain as documentation of my personal journey. Please consider this while making a contribution.

See the [open issues](https://github.com/gavinmclelland/foobar-with-Google/issues) to track a full list of proposed features (and known issues).

### How to Contribute

#### 1. Fork the Project

1. Go to the repository URL: [foobar-with-Google](https://github.com/gavinmclelland/foobar-with-Google)
2. Click on the "Fork" button at the top-right corner.
3. This will create a copy of the repository in your GitHub account.

#### 2. Clone Your Fork Locally

After forking, clone the forked repo to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/foobar-with-Google.git
```

Replace \`YOUR_USERNAME\` with your GitHub username.

#### 3. Create Your Feature Branch

Navigate to your local repository directory and execute the following:

```bash
cd foobar-with-Google
git checkout -b feature/EducationalEnhancement
```

This will create and switch to a new branch named \`feature/EducationalEnhancement\`.

#### 4. Make and Commit Your Changes

After making your changes, commit them to your feature branch:

```bash
git add .
git commit -m 'Add some EducationalEnhancement'
```

#### 5. Push Changes to GitHub

Push your committed changes from your local feature branch back to its corresponding remote feature branch on GitHub:

```bash
git push origin feature/EducationalEnhancement
```

#### 6. Open a Pull Request

Go back to your forked repository on GitHub and click "New Pull Request." Choose the feature branch you just pushed as the "compare" branch. Fill in the pull request details and submit it.

Contributions that align with the educational and journey-based nature of this repository are most welcome. Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->

## License

This work is licensed under MPL 2.0.

See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Gavin - [@gavinmclelland](https://x.com/gavinmclelland)

Project Link: [https://github.com/gavinmclelland/foobar-with-Google](https://github.com/gavinmclelland/foobar-with-Google)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Google Foobar](https://foobar.withgoogle.com/)
* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* [Development Containers](https://containers.dev/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gavinmclelland/foobar-with-Google.svg?style=for-the-badge
[contributors-url]: https://github.com/gavinmclelland/foobar-with-Google/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gavinmclelland/foobar-with-Google.svg?style=for-the-badge
[forks-url]: https://github.com/gavinmclelland/foobar-with-Google/network/members
[stars-shield]: https://img.shields.io/github/stars/gavinmclelland/foobar-with-Google.svg?style=for-the-badge
[stars-url]: https://github.com/gavinmclelland/foobar-with-Google/stargazers
[issues-shield]: https://img.shields.io/github/issues/gavinmclelland/foobar-with-Google.svg?style=for-the-badge
[issues-url]: https://github.com/gavinmclelland/foobar-with-Google/issues
[license-shield]: https://img.shields.io/github/license/gavinmclelland/foobar-with-Google.svg?style=for-the-badge
[license-url]: https://github.com/gavinmclelland/foobar-with-Google/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/gavinmclelland/
[product-screenshot]: images/screenshot.jpg
[Google]: https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=Google&logoColor=white
[google-url]: https://developers.google.com/
[visualstudiocode]: https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white
[visualstudiocode-url]: https://code.visualstudio.com/
[Docker]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white
[docker-url]: https://www.docker.com/products/docker-desktop/
[Python]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=Python&logoColor=white
[python-url]: https://www.python.org/downloads/release/python-2713/