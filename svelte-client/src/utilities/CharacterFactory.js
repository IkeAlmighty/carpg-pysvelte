import { characters } from "../stores";
import names from "./names";
import { fetchItems, fetchSpells } from "./endpoints";

const CharacterFactory = {
  ancientOne: {
    label: "Ancient One",
    generate: async (characterName, characterTier) => {
      characterName = initCharacter(
        characterName,
        CharacterFactory.ancientOne.label,
        characterTier
      );

      try {
        let res = await fetchSpells(3, [], true);

        addIncantations(characterName, res.data);

        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(
          characterName,
          "An error occured while fetching spells."
        );
      }
    },
  },
  militaryGrunt: {
    label: "Military Grunt",
    generate: async (characterName, characterTier) => {
      characterName = initCharacter(
        characterName,
        CharacterFactory.militaryGrunt.label,
        characterTier
      );

      try {
        let res = await fetchItems(1, 100, ["weapon"]);
        addInventoryItems(characterName, res.data);

        res = await fetchItems(2, 0, ["weapon"]);
        addInventoryItems(characterName, res.data);

        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(
          characterName,
          "An error occured while fetching items."
        );
      }
    },
  },
  artificer: {
    label: "Artificer",
    generate: async (characterName, characterTier) => {
      characterName = initCharacter(
        characterName,
        CharacterFactory.artificer.label,
        characterTier
      );

      try {
        let res = await fetchItems(3, 100, ["none"]);
        addInventoryItems(characterName, res.data);
        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(
          characterName,
          "An error occured while fetching items."
        );
      }
      // load the inventory of the character from the backend:
    },
  },
  medicHealer: {
    label: "Medic / Healer",
    generate: async (characterName, characterTier) => {
      characterName = initCharacter(
        characterName,
        CharacterFactory.medicHealer.label,
        characterTier
      );

      try {
        let res = await fetchItems(5, 25, [
          "consumable",
          "container",
          "trinket",
        ]);

        addInventoryItems(characterName, res.data);
        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(characterName, "Error while fetching items.");
      }
    },
  },
  diplomatLinguist: {
    label: "Diplomat / Linguist",
    generate: async (characterName, characterTier) => {
      characterName = initCharacter(
        characterName,
        CharacterFactory.diplomatLinguist.label,
        characterTier
      );

      try {
        let res = await fetchItems(1, 100, ["tool"]);
        addInventoryItems(characterName, res.data);
        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(
          characterName,
          "An error occured while fetching items"
        );
      }

      try {
        let res = await fetchSpells(1, [], true);

        addIncantations(characterName, res.data);
        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(
          characterName,
          "An error occured while fetching spells"
        );
      }
    },
  },
  npc: {
    label: "NPC",
    generate: async (characterName, characterTier) => {
      characterName = initCharacter(
        characterName,
        CharacterFactory.npc.label,
        characterTier
      );

      let itemCount = 6 - characterTier;

      try {
        let res = await fetchItems(itemCount, 100, []);
        addInventoryItems(characterName, res.data);
        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(
          characterName,
          "An error occured while fetching items"
        );
      }

      try {
        let res = await fetchSpells(Math.round(itemCount / 2), [], true);

        addIncantations(characterName, res.data);
        setLoadingMessage(characterName, undefined);
      } catch (err) {
        setLoadingMessage(
          characterName,
          "An error occured while fetching spells"
        );
      }
    },
  },
};

const generateName = () => {
  let lastName =
    names[Math.floor(Math.random() * Math.floor(names.length - 1))];
  let firstName =
    names[Math.floor(Math.random() * Math.floor(names.length - 1))];

  return firstName + " " + lastName;
};

const initCharacter = (characterName, classLabel, characterTier) => {
  if (!characterName) characterName = generateName();

  // set the initial state of the character:
  characters.update((data) => {
    data[characterName] = {
      name: characterName,
      inventory: undefined,
      incantations: undefined,
      characterClass: classLabel,
      inventoryLoadingMessage: "Generating Inventory...",
      tier: characterTier,
    };

    return data;
  });

  return characterName; //return the intialized character name (which is the id in the store)
};

const addInventoryItems = (characterName, items) => {
  // add all items in the list to the character's inventory:
  characters.update((data) => {
    let inventory = data[characterName].inventory || [];
    items.forEach((item) => inventory.push(item));
    data[characterName] = {
      name: characterName,
      inventory,
      incantations: data[characterName].incantations,
      characterClass: data[characterName].characterClass,
      inventoryLoadingMessage: data[characterName].inventoryLoadingMessage,
      tier: data[characterName].tier,
    };

    return data;
  });
};

const addIncantations = (characterName, newIncantations) => {
  characters.update((data) => {
    let incantations = data[characterName].incantations || [];
    newIncantations.forEach((incantation) => incantations.push(incantation));
    data[characterName] = {
      name: characterName,
      inventory: data[characterName].inventory,
      incantations: incantations,
      characterClass: data[characterName].characterClass,
      inventoryLoadingMessage: data[characterName].inventoryLoadingMessage,
      tier: data[characterName].tier,
    };

    return data;
  });
};

const setLoadingMessage = (characterName, message) => {
  characters.update((data) => {
    data[characterName] = {
      name: characterName,
      inventory: data[characterName].inventory,
      incantations: data[characterName].incantations,
      characterClass: data[characterName].characterClass,
      inventoryLoadingMessage: message,
      tier: data[characterName].tier,
    };

    return data;
  });
};

export default CharacterFactory;
