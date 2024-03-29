-- Plugins
require("packer").startup(function() 
    use "wbthomason/packer.nvim"
    use "kyazdani42/nvim-web-devicons"
    use "kyazdani42/nvim-tree.lua"
    use "nvim-lua/plenary.nvim"
    use "nvim-telescope/telescope.nvim"
    use "akinsho/bufferline.nvim"
    use "nvim-lualine/lualine.nvim"
    use "nvim-treesitter/nvim-treesitter"
    -- Autocompletion and LSP
    use "neovim/nvim-lspconfig"
    use "williamboman/nvim-lsp-installer"
    use "hrsh7th/nvim-cmp"
    use "hrsh7th/cmp-nvim-lsp"
    use "hrsh7th/cmp-buffer"
    use "hrsh7th/cmp-path"
    use "hrsh7th/cmp-cmdline"
    use "L3MON4D3/LuaSnip"
    use "saadparwaiz1/cmp_luasnip"
    -- Startup
    use {
        "startup-nvim/startup.nvim",
        requires = {"nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim"},
        config = function()
            require"startup".setup()
        end
    }
    -- Themes
    use {
        "loctvl842/monokai-pro.nvim",
        config = function()
            require("monokai-pro").setup()
        end
    }
    use "navarasu/onedark.nvim"
    use "tiagovla/tokyodark.nvim"
    use "folke/tokyonight.nvim"
end)

-- NvimTree
require("nvim-tree").setup {}
-- Bufferline
require("bufferline").setup {}
-- Lualine
require("lualine").setup {
    options = {
        section_separators = { left = "" , right = "" },
        theme = "monokai-pro"
    }
}
-- Colorscheme
-- monokai-pro
vim.cmd([[colorscheme monokai-pro]])
-- tokyonight
-- vim.cmd("colorscheme tokyonight")
-- tokyodark
-- vim.cmd("colorscheme tokyodark")
-- onedark darker 
--[[require("onedark").setup {
	style = "darker",
    transparent = true,
}
require("onedark").load()
--]]
-- Treesitter
require("nvim-treesitter.configs").setup {
    highlight = { enable = true },
    indent = { enable = false }
}
-- LspInstaller
require("nvim-lsp-installer").setup({
    automatic_installation = true,
})
