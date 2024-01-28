import React from "react";
import LogoutButton from "./logout";

type NavbarProps = {
    name: string,
    image: string
}

export default function Navbar(props: NavbarProps): JSX.Element {

    return (
        <div className="text-red-800 w-full h-auto flex flex-row gap-8 px-4 py-2 items-center justify-between bg-gradient-to-r from-orange-300 to-orange-500 flex-wrap">
            <div className="md:px-10 px-4 md:text-2xl text-xl flex flex-row gap-6 ">
                <a className="hover:text-black transition-all" href="/profile">Home</a>
                <a className="hover:text-black transition-all" href="/stats">Tracker</a>
            </div>
            <div className="md:px-10 px-4 md:text-xl text-md flex flex-col md:flex-row items-center md:gap-8 justify-end">
                <img className="rounded-full w-16" src={props.image} alt={props.name} />
                <LogoutButton />
            </div>
        </div>
    )

}