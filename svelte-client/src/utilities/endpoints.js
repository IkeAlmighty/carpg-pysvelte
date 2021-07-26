import axios from "axios";

const fetchTags = (tagType) => {
  return axios.get(`_ENV_API_URI/tags?tagtype=${tagType}`);
};

// helper function
const stringifyTags = (tags) => {
  let tagsString = undefined;
  if (tags.length === 0) {
    tagsString = "any,none";
  } else {
    tagsString = tags.reduce((acc, curr) => {
      return acc + "," + curr;
    });
  }
  return tagsString;
};

const fetchItems = (limit, spellchance, tags, seed) => {
  return axios.get(
    `_ENV_API_URI/items?limit=${limit}&spellchance=${spellchance}&seed=${seed}&tags=${stringifyTags(
      tags
    )}`
  );
};

const fetchSpells = (limit, tags, onlyincantations) => {
  return axios.get(
    `_ENV_API_URI/spells?limit=${limit}&onlyincantations=${onlyincantations}&tags=${stringifyTags(
      tags
    )}`
  );
};

const fetchIncantations = (text) => {
  return axios.get(`_ENV_API_URI/incantions`);
};

const fetchTranslation = (text, seed) => {
  return axios.get(`_ENV_API_URI/translate?text=${text}&seed=${seed}`);
};

const fetchRules = () => {
  // return axios.get(`ENV_API_URI/rules`);
  return axios.get(
    "https://docs.googleapis.com/v1/documents/1SVGhe15qIAoNtpIjSl6rLovofYXPrDpKcl1pQtiMhZk"
  );
};

export {
  fetchTags,
  fetchItems,
  fetchSpells,
  fetchTranslation,
  fetchIncantations,
  fetchRules,
};
