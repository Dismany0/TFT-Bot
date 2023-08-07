import { Client } from "discord.js";
import token from "./token.json";

console.log("Bot is starting...");

const client = new Client({
    intents: []
});
client.login(token["TOKEN"]);

console.log(client)