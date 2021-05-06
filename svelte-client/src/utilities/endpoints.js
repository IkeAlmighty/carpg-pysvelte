import axios from "axios";

const fetchTags = () => {
  return axios.get("_ENV_API_URI/tags");
};

// helper function
const stringifyTags = (tags) => {
  let tagsString = undefined;
  if (tags.length === 0) {
    tagsString = "any";
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

const fetchSpells = (limit, tags) => {
  return axios.get(
    `_ENV_API_URI/spells?limit=${limit}&tags=${stringifyTags(tags)}`
  );
};

const fetchIncantations = (text) => {
  return axios.get(`_ENV_API_URI/incantions`);
};

const fetchTranslation = (text, seed) => {
  return axios.get(`_ENV_API_URI/translate?text=${text}&seed=${seed}`);
};

export {
  fetchTags,
  fetchItems,
  fetchSpells,
  fetchTranslation,
  fetchIncantations,
};
