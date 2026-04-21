# User Specifications
This document defines the constraints and requirements for user accounts, including usernames, passwords, and profile pictures.

## Username Constraints
Each user must have a username that satisfies the following:
- **Uniqueness**: Must be unique across the system
- **Length**: Between **3 and 32 characters** (inclusive)
- **Allowed characters**:
  - Lowercase letters (`a–z`)
  - Digits (`0–9`)
  - Hyphen (`-`)
  - Underscore (`_`)
- **Restrictions**:
  - No spaces or other special characters
  - Cannot start or end with a hyphen or underscore

## Password Constraints
Each user must have a password that meets the following:
- **Length**: Between **6 and 32 characters** (inclusive)
- Maximum length of 32 characters

## Profile Picture Constraints
A profile picture is stored as a reference (e.g., URL or identifier) to an external image.
- **Reference length**: Must be **less than 128 characters**
- **Format**: Must be a valid URL or system-recognized image reference
