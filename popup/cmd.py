from popup.tasks.main import *
from popup.tasks.shell import *
from popup.tasks.group import *
HOME = os.environ['HOME']

git_package = Package("git")

dotfiles = Git("https://github.com/jared-skinner/dotfiles.git", target="dotfiles")
df_path = dotfiles.target

zsh = Package("zsh")
fzf = Package("fzf")
rg = Package("ripgrep")
htop = Package("htop")
bat = Package("bat")
node = Package("nodejs")
npm = Package("npm")

if platform in ("linux", "linux2"):
    appimage = Group(name = "appimage", deps = [
        Package("libfuse2"),
    ])

    neovim = Group("nvim_group", deps = [
        fzf,
        rg,
        node,
        npm,
        appimage,
        Bash(name="nvim_appimage", comand=f"curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage --output-dir {HOME}/.local/bin", deps=[appimage]),
        Bash(name="nvim_change_perms", comand=f"chmod u+x {HOME}/.local/bin/nvim.appimage", deps=[appimage]),
    ])
else:
    neovim = Package("neovim", deps = [
        fzf,
        rg,
        node,
        npm,
    ])

cmd_packages = Group(name = "packages", deps = [
    zsh,
    fzf,
    rg,
    htop,
    node,
    npm,
    bat,
    neovim
])

ohmyzsh_git = Git("https://github.com/ohmyzsh/ohmyzsh.git", target="ohmyzsh")
ohmyzsh_path = ohmyzsh_git.target

ohmyzsh = Group("ohmyzsh", force=True, deps = [
    ohmyzsh_git,
    Copy(src = f"{ohmyzsh_path}", dest=f"{HOME}/.oh-my-zsh"),
])

copy_dots = Group(name = "copy_dots", deps = [
    Copy(
        src = os.path.join(df_path, ".gitconfig"),
        dest = f"{HOME}/.gitconfig",
        deps = [git_package, dotfiles]
    ),
    Copy(
        src=os.path.join(df_path, "nvim"),
        dest= f"{HOME}/.config/nvim",
        deps=[fzf, rg, dotfiles]
    ),
    Copy(
        src=os.path.join(df_path, ".tmux"),
        dest= f"{HOME}/.tmux",
        deps=[Package("tmux"), dotfiles]
    ),
    Copy(
        src = os.path.join(df_path, ".zshrc"),
        dest = f"{HOME}/.zshrc",
        force=True,
        overwrite=True
    ),
    Copy(
        src = os.path.join(df_path, ".profile"),
        dest = f"{HOME}/.profile",
        overwrite = True
    )
], force=True)

main_task = Main(name="cmd_work", deps=[
    copy_dots,
    cmd_packages,
])
