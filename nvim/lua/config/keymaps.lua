-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local function map(mode, lhs, rhs, opts)
  local options = { noremap = true }
  if opts then
    options = vim.tbl_extend("force", options, opts)
  end
  vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

map("i", "jk", "<esc>") -- use jk for exiting insert mode
map("t", "jk", "<esc>") -- use jk for exiting terminal mode
map("n", "<space>", "za") -- space open/closes folds
map("n", "<F7>", ":setlocal spell! spelllang=en_us<CR>") -- toggle spellcheck
map("n", "<Tab>", ":bnext<CR>") -- tab -> next buffer
map("n", "<S-Tab>", ":bprevious<CR>") -- shift + tab -> previous buffer
map("n", "j", "gj") -- move vertically by visual line
map("n", "k", "gk") -- move vertically by visual line
map("n", "<leader>w", ":set wrap!<CR>") -- toggle wrap
map("n", "<CR>", ":set hlsearch! hlsearch?<CR>") -- return turns off search highlighting

vim.keymap.set(
  "n",
  "<leader>fa",
  ":Telescope find_files find_command=rg,--files,/Users/jaredskinner/src/server/analytics,/Users/jaredskinner/src/server/dropbox/apx,/Users/jaredskinner/src/server/dropbox/airflow,/Users/jaredskinner/src/server/dropbox/analytics,/Users/jaredskinner/src/server/dropbox/di<CR>",
  { noremap = true, silent = true, desc = "Search Directories important to analytics" }
)

-- TODO
-- tab complete to next option when available
function _G.tab_complete()
  if vim.fn.pumvisible() == 1 then
    return vim.api.nvim_replace_termcodes("<C-n>", true, true, true)
  else
    return vim.api.nvim_replace_termcodes("<Tab>", true, true, true)
  end
end
map("i", "<TAB>", "v:lua.tab_complete()", { expr = true, noremap = true }) -- if multiple auto-complete options
map("n", "<C-p>", ":SearchAnalytics<CR>")
