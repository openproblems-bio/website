-- Glossary.lua
-- Authors: Lisa DeBruine, Robrecht Cannoodt

glossary = nil

local function labelToKey(str)
  local lower = string.lower(str)
  -- replace non-alphanumeric characters with dashes
  local noSpaces = string.gsub(lower, "[^%w]", "-")
  return noSpaces
end

local function readGlossary(meta)
  -- get glossary path
  local path = "glossary.yml"
  if meta.glossary ~= nil then
    path = pandoc.utils.stringify(meta.glossary)
  end
  
  local file = io.open(path, "rb")
  local data
  if file then
    data = file:read('*all')
    file:close()
  end
  if data == nil then
    return {}
  end
  local content = "---\n" .. data .. "\n---\n"
  local glossary = pandoc.read(content, "markdown").meta

  local toLowerGlossary = {}
  for label, value in pairs(glossary) do
    toLowerGlossary[labelToKey(label)] = {
      ["label"] = label,
      ["value"] = value
    }
  end

  return toLowerGlossary
end

-- Main Glossary Function Shortcode

return {
  ["glossary"] = function(args, kwargs2, meta)
    -- this will only run for HTML documents
    if not quarto.doc.isFormat("html:js") then
      return pandoc.Null()
    end

    -- fix issue with kwargs
    local kwargs = {}
    for key, value in pairs(kwargs2) do
      kwargs[string.lower(key)] = value
    end

    -- read glossary if not already read
    if glossary == nil then
      glossary = readGlossary(meta)
    end
    
    -- if no arguments, create glossary
    if #args == 0 then
      -- sort keys
      local keys = {}
      for key in pairs(glossary) do
        table.insert(keys, key)
      end
      table.sort(keys)
      -- print glossary
      local str = ""
      for _, key in ipairs(keys) do
        local value = glossary[key]
        str = str .. "#### " .. value.label .. "{#" .. key .. "}\n\n"
        str = str .. pandoc.utils.stringify(value.value) .. "\n\n"
      end

      return pandoc.read(str, "markdown").blocks
    else
      -- if argument, create link
      local label = table.concat(args, " ")
      local term = labelToKey(label)

      if glossary[term] == nil then
        return pandoc.Str(label)
      end

      -- check if custom display is provided
      if kwargs.label ~= nil then
        label = pandoc.utils.stringify(kwargs["label"])
      end

      -- return link
      local url = "/documentation/reference/glossary/index.qmd#" .. term
      local link = pandoc.Link(label, url, "", pandoc.Attr("class", {"quarto-xref"}))
      return link
    end
  end
}
