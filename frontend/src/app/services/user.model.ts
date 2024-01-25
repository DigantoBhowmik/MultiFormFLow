export interface CreateUserDto {
    email: string;
    instraFile: File;
    ytUsername: string;
    ytcFile: File;
    ytUrl: string;
    [key: string]: any;
}

export interface UserDto {
    email: string;
    is_instra_ss: boolean;
    yt_username: string;
    is_ytc_ss: boolean;
    yt_url: string;
}