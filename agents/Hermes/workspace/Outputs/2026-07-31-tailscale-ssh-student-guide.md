# Remote Access Between Two Macs with Tailscale + SSH

> A beginner-friendly guide for securely controlling a Mac at home from another Mac—without opening router ports or exposing the home Mac directly to the internet.

**Difficulty:** Beginner  
**Time needed:** About 10–15 minutes  
**You need:** Two Macs, internet access, and permission to install apps and change Sharing settings on both devices

---

## What you are setting up

You will connect:

- **Home Mac:** The Mac you want to access remotely. It stays at home.
- **Travel Mac:** The MacBook you carry and use to connect.

Tailscale creates a private encrypted network between the two Macs. SSH is the secure command-line door into the Home Mac.

**Simple mental model:** Tailscale creates a private road. SSH is the locked door at the end of that road.

### What this guide does not require

- No router configuration
- No port forwarding
- No public IP address
- No paid server
- No sharing your Mac password with Tailscale

> **Important:** This guide uses normal macOS Remote Login over Tailscale. It does not use Tailscale’s separate “Tailscale SSH server” feature, which requires a different command-line-only Tailscale installation on macOS.

---

## Before you begin

Have both Macs in front of you for the initial setup. Confirm that:

- Both Macs use macOS Monterey 12 or newer.
- You know the administrator password for each Mac.
- You have a Tailscale account—or can create one using Google, Microsoft, GitHub, Apple, or another supported sign-in provider.
- The Home Mac can remain powered on and connected to the internet when you are away.

Official links:

- [Download Tailscale for macOS](https://tailscale.com/docs/install/mac)
- [Open the Tailscale Machines page](https://login.tailscale.com/admin/machines)
- [Apple’s Remote Login instructions](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)

---

# Part 1 — Install Tailscale on both Macs

Repeat these steps on the **Home Mac** and the **Travel Mac**.

1. Go to [Tailscale for macOS](https://tailscale.com/docs/install/mac).
2. Download the recommended **Standalone** version, or install Tailscale from the Mac App Store.
3. Open Tailscale.
4. Approve the macOS VPN/network-extension request if macOS asks.
5. Click **Log in**.
6. Sign in using the **same Tailscale account** on both Macs.
7. Confirm that Tailscale says **Connected** on both devices.

### Quick check

Open the [Tailscale Machines page](https://login.tailscale.com/admin/machines). You should see both Macs listed and marked as connected.

> If the Macs appear under different Tailscale accounts or different tailnets, they will not see each other. Sign both into the same account unless your organization’s administrator has intentionally invited both accounts into one tailnet.

---

# Part 2 — Prepare the Home Mac

Do the following on the Mac that will stay at home.

## Step 1: Give the Home Mac a clear name

1. Open **System Settings**.
2. Go to **General → About**.
3. Click the current computer name.
4. Use a simple name such as `home-mac`, `office-mac`, or `studio-mac`.

A clear name makes the device easier to recognize in Tailscale.

## Step 2: Turn on Remote Login

1. Open **System Settings**.
2. Go to **General → Sharing**.
3. Find **Remote Login**.
4. Turn **Remote Login** on.
5. Click the information button beside Remote Login.
6. Under **Allow access for**, choose **Only these users**.
7. Add only the Mac account that should be allowed to connect.

For a personal machine, allowing only your own user account is safer than allowing all users.

> You normally do not need **Allow full disk access for remote users** just to use SSH. Leave it off unless you understand why you need it.

## Step 3: Find the Home Mac’s username

1. Open **Terminal**. You can find it using Spotlight: press `Command + Space`, type `Terminal`, and press Return.
2. Paste this command and press Return:

```bash
whoami
```

Terminal will print a name such as:

```text
alex
```

Write it here:

```text
HOME MAC USERNAME: ______________________________
```

The username is usually short and lowercase. It may be different from the full name shown on the login screen.

## Step 4: Find the Home Mac’s Tailscale address

The easiest method is the Tailscale Machines page:

1. Open [Tailscale Machines](https://login.tailscale.com/admin/machines).
2. Find the Home Mac.
3. Copy its Tailscale IPv4 address. It normally begins with `100.`.
4. You may also see a device name such as `home-mac` or a full MagicDNS name.

Write down at least one address:

```text
TAILSCALE IP:      100.____.____.____
DEVICE NAME:       ______________________________
MAGICDNS NAME:     ______________________________
```

## Step 5: Keep the Home Mac available

SSH cannot reach a Mac that is fully shut down or disconnected from the internet.

- Keep the Home Mac powered on.
- Keep Tailscale connected.
- If it is a MacBook, connect it to power.
- In **System Settings → Battery → Options**, consider enabling the setting that prevents automatic sleep on the power adapter when the display is off.
- On a desktop Mac, review **System Settings → Energy Saver** and enable wake/network access options that fit your needs.

The display may be off. The Mac itself must remain awake enough to accept network connections.

---

# Part 3 — Connect from the Travel Mac

Do these steps on the MacBook or other Mac you are using away from home.

## Step 1: Confirm Tailscale is connected

Open Tailscale and confirm it says **Connected**. The Home Mac should appear on the Machines page.

## Step 2: Open Terminal

Press `Command + Space`, type `Terminal`, and press Return.

## Step 3: Connect with SSH

Use this format:

```bash
ssh HOME_USERNAME@TAILSCALE_IP
```

Example:

```bash
ssh alex@100.80.20.15
```

If MagicDNS is enabled, you can usually use the Tailscale device name instead:

```bash
ssh alex@home-mac
```

Or use the full MagicDNS name shown in Tailscale:

```bash
ssh alex@home-mac.example-tailnet.ts.net
```

Replace the example username and address with the values you wrote down from your Home Mac.

## Step 4: Approve the Home Mac the first time

The first connection may show a message similar to:

```text
The authenticity of host ... can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Confirm that the address or device name is your Home Mac. Then type:

```text
yes
```

Press Return.

> If this warning appears unexpectedly after you have connected successfully many times, stop and verify that the Home Mac was not erased, reinstalled, or replaced before accepting a changed fingerprint.

## Step 5: Enter the Home Mac password

Enter the password for the **Home Mac user account**, then press Return.

Terminal will not display dots, stars, or moving characters while you type the password. This is normal.

Do not use your Tailscale password unless it happens to be the same as the Home Mac login password.

## Step 6: Confirm that the connection worked

After connecting, run:

```bash
whoami
scutil --get ComputerName
```

You should see the Home Mac username and computer name.

You can also run:

```bash
pwd
```

This shows the folder you are currently in on the Home Mac.

## Step 7: Disconnect safely

When finished, run:

```bash
exit
```

You will return to the Travel Mac’s normal Terminal prompt.

---

# Copy-and-paste connection template

Complete these values:

```text
Home Mac username: ______________________________
Home Mac Tailscale IP: __________________________
Home Mac device name: ___________________________
```

Build your command:

```bash
ssh YOUR_HOME_USERNAME@YOUR_TAILSCALE_IP
```

Example only:

```bash
ssh alex@100.80.20.15
```

---

# Optional — Test before attempting login

From the Travel Mac, test whether the Home Mac’s SSH door is reachable:

```bash
nc -zv YOUR_TAILSCALE_IP 22
```

A successful result looks similar to:

```text
Connection to 100.x.x.x port 22 [tcp/ssh] succeeded!
```

This proves that the network path and Remote Login service are reachable. It does not test the username or password.

---

# Troubleshooting

## “Connection timed out”

Check these items:

- Tailscale is connected on both Macs.
- Both Macs appear online on the Tailscale Machines page.
- The Home Mac is powered on and awake.
- Both devices are in the same tailnet.
- Tailscale’s **Block incoming connections** or **Shields Up** option is not enabled on the Home Mac.

## “Connection refused”

The Home Mac is reachable, but Remote Login is probably off.

On the Home Mac, return to:

**System Settings → General → Sharing → Remote Login**

Turn it on and confirm your account is allowed.

## “Permission denied”

The network connection worked, but the login was rejected.

- Run `whoami` directly on the Home Mac and use that exact username.
- Enter the Home Mac’s login password—not the Travel Mac password.
- In Remote Login settings, confirm that the user is included under **Allow access for**.
- Remember that Terminal shows no characters while you type a password.

## The Home Mac disappears while you are away

The Home Mac may be asleep, shut down, offline, or disconnected from Tailscale. Review its power settings before leaving home.

## The device name does not work, but the IP works

Use the `100.x.x.x` Tailscale IP. Then check whether MagicDNS is enabled in the Tailscale admin console.

## “Host key verification failed” or a fingerprint changed

Do not blindly delete security records. First confirm whether the Home Mac was erased, reinstalled, renamed, or replaced. Ask a teacher or administrator if you are unsure.

---

# Security checklist

- Use **Only these users** in Remote Login settings.
- Never share your Mac password in chat, email, or screenshots.
- Never forward router port `22` to the internet for this setup.
- Remove old or lost devices from the Tailscale Machines page.
- Keep macOS and Tailscale updated.
- Use a strong login password and enable FileVault on portable Macs.
- Turn off Remote Login if you no longer need SSH access.
- If a travel device is lost, immediately remove it from Tailscale.

---

# Optional advanced step — Passwordless login with an SSH key

Passwordless login is convenient, but beginners should first confirm that password-based SSH works. Then ask an instructor or administrator to help install an SSH public key from the Travel Mac onto the Home Mac.

Never send or copy a file named `id_ed25519` or any other **private key**. Only the file ending in `.pub` is designed to be shared.

---

# One-minute final test

Before leaving home:

1. Confirm Tailscale is connected on both Macs.
2. Confirm Remote Login is on for the Home Mac.
3. On the Travel Mac, connect using `ssh username@100.x.x.x`.
4. Run `whoami` and confirm it shows the Home Mac username.
5. Run `scutil --get ComputerName` and confirm it shows the Home Mac name.
6. Run `exit`.
7. Test once more using the Travel Mac on a different internet connection, such as a phone hotspot.

> **Success means:** You can securely open an SSH session from the Travel Mac to the Home Mac through Tailscale, without changing router settings or exposing SSH directly to the public internet.

---

## Official references

- [Tailscale: Install on macOS](https://tailscale.com/docs/install/mac)
- [Tailscale: macOS variants](https://tailscale.com/docs/concepts/macos-variants)
- [Tailscale: Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh)
- [Apple: Allow a remote computer to access your Mac](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)

*Prepared as a beginner-friendly Limitless Club student resource. Menu labels can vary slightly between macOS versions.*
