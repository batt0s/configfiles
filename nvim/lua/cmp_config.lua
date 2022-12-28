local cmp = require("cmp")
local luasnip = require("luasnip")
local select_opts = { behavior = cmp.SelectBehavior.Select }
cmp.setup({
    snippet = {
        expand = function(args) luasnip.lsp_expand(args.body) end
    },
    sources = {
        { name = "path" },
        { name = "nvim_lsp" , keyword_length = 3 },
        { name = "buffer" , keyword_length = 3 },
        { name = "luasnip" , keyword_length = 2 },
    },
    window = {
        completion = cmp.config.window.bordered(),
        documentation = cmp.config.window.bordered()
    },
    mapping = {
        ["<Up>"] = cmp.mapping.select_prev_item(select_opts),
        ["<Down>"] = cmp.mapping.select_next_item(select_opts),
        
        ["<C-p>"] = cmp.mapping.select_prev_item(select_opts),
        ["<C-n>"] = cmp.mapping.select_next_item(select_opts),

        ["<C-u>"] = cmp.mapping.scroll_docs(-4),
        ["<C-f>"] = cmp.mapping.scroll_docs(4),

        ["<C-e>"] = cmp.mapping.abort(),

        ["<CR>"] = cmp.mapping.confirm({ select = true }),

        ["<Tab>"] = cmp.mapping(function(fallback) 
            local col = vim.fn.col(".") - 1 

            if cmp.visible() then 
                cmp.select_next_item(select_opts)
            elseif col == 0 or vim.fn.getline("."):sub(col,col):match("%s") then
                fallback()
            else
                cmp.complete()
            end
        end, { "i" , "s" }),
    }
})
