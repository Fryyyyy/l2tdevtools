#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the download helper object implementations."""

import shlex
import subprocess
import unittest

from l2tdevtools.download_helpers import github

from tests import test_lib


class DocoptGitHubReleasesDownloadHelperTest(test_lib.BaseTestCase):
  """Tests for the docopt GitHub releases download helper."""

  _DOWNLOAD_URL = 'https://github.com/docopt/docopt/releases'
  _GIT_URL = 'https://github.com/docopt/docopt.git'

  _PROJECT_ORGANIZATION = 'docopt'
  _PROJECT_NAME = 'docopt'
  _PROJECT_VERSION = '0.6.2'

  @classmethod
  def setUpClass(cls):
    """Determines the project version from the latest git tag."""
    command = 'git ls-remote --tags {0:s}'.format(cls._GIT_URL)
    arguments = shlex.split(command)

    try:
      process = subprocess.Popen(
          arguments, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except OSError:
      return

    output, _ = process.communicate()
    if process.returncode != 0:
      return

    output = output.decode('ascii')

    latest_version = ('0', '0', '0')
    for line in output.split('\n'):
      line = line.strip()
      if 'refs/tags/' in line and not line.endswith('^{}'):
        _, _, version = line.rpartition('refs/tags/')
        version = tuple(version.split('.'))
        latest_version = max(latest_version, version)

    cls._PROJECT_VERSION = '.'.join(latest_version)

  def testGetLatestVersion(self):
    """Tests the GetLatestVersion functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    latest_version = download_helper.GetLatestVersion(self._PROJECT_NAME, None)

    self.assertEqual(latest_version, self._PROJECT_VERSION)

  def testGetDownloadURL(self):
    """Tests the GetDownloadURL functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    download_url = download_helper.GetDownloadURL(
        self._PROJECT_NAME, self._PROJECT_VERSION)

    expected_download_url = (
        'https://github.com/{0:s}/{1:s}/archive/refs/tags/{2:s}.tar.gz').format(
            self._PROJECT_ORGANIZATION, self._PROJECT_NAME,
            self._PROJECT_VERSION)

    self.assertEqual(download_url, expected_download_url)

  def testGetProjectIdentifier(self):
    """Tests the GetProjectIdentifier functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    project_identifier = download_helper.GetProjectIdentifier()

    expected_project_identifier = 'com.github.{0:s}.{1:s}'.format(
        self._PROJECT_ORGANIZATION, self._PROJECT_NAME)

    self.assertEqual(project_identifier, expected_project_identifier)


class LibyalGitHubReleasesDownloadHelperTest(test_lib.BaseTestCase):
  """Tests for the libyal GitHub releases download helper."""

  _DOWNLOAD_URL = 'https://github.com/libyal/libevt/releases'
  _GIT_URL = 'https://github.com/libyal/libevt.git'

  _PROJECT_ORGANIZATION = 'libyal'
  _PROJECT_NAME = 'libevt'
  _PROJECT_STATUS = 'alpha'
  _PROJECT_VERSION = '20210424'

  @classmethod
  def setUpClass(cls):
    """Determines the project version from the latest git tag."""
    command = 'git ls-remote --tags {0:s}'.format(cls._GIT_URL)
    arguments = shlex.split(command)

    try:
      process = subprocess.Popen(
          arguments, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except OSError:
      return

    output, _ = process.communicate()
    if process.returncode != 0:
      return

    output = output.decode('ascii')

    latest_version = '0'
    for line in output.split('\n'):
      line = line.strip()
      if 'refs/tags/' in line and not line.endswith('^{}'):
        _, _, version = line.rpartition('refs/tags/')
        latest_version = max(latest_version, version)

    cls._PROJECT_VERSION = latest_version

  def testGetLatestVersion(self):
    """Tests the GetLatestVersion functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    latest_version = download_helper.GetLatestVersion(self._PROJECT_NAME, None)

    self.assertEqual(latest_version, self._PROJECT_VERSION)

  def testGetDownloadURL(self):
    """Tests the GetDownloadURL functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    download_url = download_helper.GetDownloadURL(
        self._PROJECT_NAME, self._PROJECT_VERSION)

    expected_download_url = (
        'https://github.com/{0:s}/{1:s}/releases/download/{3:s}/'
        '{1:s}-{2:s}-{3:s}.tar.gz').format(
            self._PROJECT_ORGANIZATION, self._PROJECT_NAME,
            self._PROJECT_STATUS, self._PROJECT_VERSION)

    self.assertEqual(download_url, expected_download_url)

  def testGetProjectIdentifier(self):
    """Tests the GetProjectIdentifier functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    project_identifier = download_helper.GetProjectIdentifier()

    expected_project_identifier = 'com.github.{0:s}.{1:s}'.format(
        self._PROJECT_ORGANIZATION, self._PROJECT_NAME)

    self.assertEqual(project_identifier, expected_project_identifier)


class Log2TimelineGitHubReleasesDownloadHelperTest(test_lib.BaseTestCase):
  """Tests for the log2timeline GitHub releases download helper."""

  _DOWNLOAD_URL = 'https://github.com/log2timeline/dfvfs/releases'
  _GIT_URL = 'https://github.com/log2timeline/dfvfs.git'

  _PROJECT_ORGANIZATION = 'log2timeline'
  _PROJECT_NAME = 'dfvfs'
  _PROJECT_VERSION = '20210728'

  @classmethod
  def setUpClass(cls):
    """Determines the project version from the latest git tag."""
    command = 'git ls-remote --tags {0:s}'.format(cls._GIT_URL)
    arguments = shlex.split(command)

    try:
      process = subprocess.Popen(
          arguments, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except OSError:
      return

    output, _ = process.communicate()
    if process.returncode != 0:
      return

    output = output.decode('ascii')

    latest_version = '0'
    for line in output.split('\n'):
      line = line.strip()
      if 'refs/tags/' in line and not line.endswith('^{}'):
        _, _, version = line.rpartition('refs/tags/')
        latest_version = max(latest_version, version)

    cls._PROJECT_VERSION = latest_version

  def testGetLatestVersion(self):
    """Tests the GetLatestVersion functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    latest_version = download_helper.GetLatestVersion(self._PROJECT_NAME, None)

    self.assertEqual(latest_version, self._PROJECT_VERSION)

  def testGetDownloadURL(self):
    """Tests the GetDownloadURL functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    download_url = download_helper.GetDownloadURL(
        self._PROJECT_NAME, self._PROJECT_VERSION)

    expected_download_url = (
        'https://github.com/{0:s}/{1:s}/releases/download/{2:s}/'
        '{1:s}-{2:s}.tar.gz').format(
            self._PROJECT_ORGANIZATION, self._PROJECT_NAME,
            self._PROJECT_VERSION)

    self.assertEqual(download_url, expected_download_url)

  def testGetProjectIdentifier(self):
    """Tests the GetProjectIdentifier functions."""
    download_helper = github.GitHubReleasesDownloadHelper(self._DOWNLOAD_URL)

    project_identifier = download_helper.GetProjectIdentifier()

    expected_project_identifier = 'com.github.{0:s}.{1:s}'.format(
        self._PROJECT_ORGANIZATION, self._PROJECT_NAME)

    self.assertEqual(project_identifier, expected_project_identifier)


if __name__ == '__main__':
  unittest.main()
