-- Keymaps
vim.g.mapleader = " "

local function map(mode, shortcut, command)
    vim.api.nvim_set_keymap(mode, shortcut, command, { noremap = true, silent = true })
end

local function nmap(shortcut, command)
    map("n", shortcut, command)
end

local function imap(shortcut, command)
    map("i", shortcut, command)
end

nmap("<leader>ff", "<cmd>Telescope find_files<cr>")
nmap("<leader>fb", "<cmd>Telescope buffers<cr>")
nmap("<leader>bn", ":bn<CR>")
nmap("<leader>bp", ":bp<CR>")
nmap("<leader>bd", ":bd<CR>")
nmap("<C-n>", ":NvimTreeToggle<CR>")
nmap("<leader>h", "<C-w>h")
nmap("<leader>j", "<C-w>j")
nmap("<leader>k", "<C-w>k")
nmap("<leader>l", "<C-w>l")

imap("\"", "\"\"<left>")
imap("'", "''<left>")
imap("(", "()<left>")
imap("{", "{}<left>")
imap("[", "[]<left>")
